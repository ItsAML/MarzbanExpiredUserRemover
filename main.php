<?php
require 'vendor/autoload.php'; // Assuming you have Composer and Guzzle installed

use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;
use GuzzleHttp\Psr7\Request;

// Constants
define('DOMAIN', 'YOUR_DOMAIN');
define('PORT', 443);
define('USERNAME', 'YOUR_USERNAME');
define('PASSWORD', 'YOUR_PASSWORD');

// Create a Guzzle HTTP client
$client = new Client();

function getAccessToken($username, $password) {
    $url = "https://" . DOMAIN . ":" . PORT . "/api/admin/token";
    $data = [
        'username' => $username,
        'password' => $password,
    ];

    try {
        $response = $client->post($url, [
            'form_params' => $data,
        ]);
        $jsonResponse = json_decode($response->getBody(), true);
        $access_token = $jsonResponse['access_token'];
        echo ".:Logged in Successfully:.\n";
        return $access_token;
    } catch (RequestException $e) {
        error_log("Error occurred while obtaining access token: " . $e->getMessage());
        return null;
    }
}

function getUsersList($access_token) {
    $url = "https://" . DOMAIN . ":" . PORT . "/api/users?status=expired";
    $headers = [
        'headers' => [
            'accept' => 'application/json',
            'Authorization' => 'Bearer ' . $access_token,
        ],
    ];

    try {
        $response = $client->get($url, $headers);
        $users_list = json_decode($response->getBody(), true);
        return $users_list;
    } catch (RequestException $e) {
        error_log("Error occurred while retrieving users list: " . $e->getMessage());
        return null;
    }
}

function removeExpiredUsers($access_token, $exp_user) {
    $url = "https://" . DOMAIN . ":" . PORT . "/api/user/{$exp_user}";
    $headers = [
        'headers' => [
            'accept' => 'application/json',
            'Authorization' => 'Bearer ' . $access_token,
            'Content-Type' => 'application/json',
        ],
    ];

    try {
        $response = $client->delete($url, $headers);
        $user_details = json_decode($response->getBody(), true);
        return true;
    } catch (RequestException $e) {
        error_log("Error occurred while modifying user data limit: " . $e->getMessage());
        return false;
    }
}

// Main script
$access_token = getAccessToken(USERNAME, PASSWORD);
if ($access_token) {
    $users_list = getUsersList($access_token);
    if ($users_list) {
        $expired_users = [];
        foreach ($users_list['users'] as $user) {
            $matches = [];
            if (preg_match("/'username'\s*:\s*'(\w+)'/", json_encode($user), $matches)) {
                $expired_users[] = $matches[1];
            }
        }

        // Count and print the number of expired users
        $num_expired_users = count($expired_users);
        echo "Total expired users: $num_expired_users\n";

        foreach ($expired_users as $i) {
            if (removeExpiredUsers($access_token, $i)) {
                echo "User $i has been successfully removed.\n";
            } else {
                echo "Failed to remove user $i.\n";
            }
        }

        echo "All expired users have been processed.\n";
    }
}
?>
