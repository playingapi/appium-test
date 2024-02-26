#!/usr/bin/env python
# -*- coding: utf-8-*-
#pip install Appium-Python-Client
#pip install selenium

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.options.android import UiAutomator2Options
#import requests
#import json
import random
from time import sleep
import getopt
import os,sys


deviceList = {}


'''
response = requests.get("https://testingbot.com/api/v1/devices?web=1")
data = response.json()

for item in data:
    if item["platform_name"] == "Android":
        print(item["name"] + " " + item["test_environment"]["version"])
        #testingbotDeviceList.append({"deviceName" : item["name"], "platformName" : item["platform_name"], "version" : item["test_environment"]["version"]})
'''

testingbotDeviceList = [{
    "platformName": "Android",
    "deviceName": "Galaxy S8",
    "version": "9.0"
}, {
    "platformName": "Android",
    "deviceName": "Pixel",
    "version": "7.1"
}, {
    "platformName": "Android",
    "deviceName": "Galaxy S10",
    "version": "10.0"
}, {
    "platformName": "Android",
    "deviceName": "Galaxy Tab A",
    "version": "9.0"
}, {
    "platformName": "Android",
    "deviceName": "Galaxy S20",
    "version": "10.0"
}, {
    "platformName": "Android",
    "deviceName": "Galaxy S21",
    "version": "11.0"
}, {
    "platformName": "Android",
    "deviceName": "Mi 10",
    "version": "12.0"
}, {
    "platformName": "Android",
    "deviceName": "Galaxy A12",
    "version": "11.0"
}, {
    "platformName": "Android",
    "deviceName": "OnePlus 9",
    "version": "11.0"
}, {
    "platformName": "Android",
    "deviceName": "Galaxy S23",
    "version": "13.0"
}, {
    "platformName": "Android",
    "deviceName": "Pixel 8",
    "version": "14.0"
}]

bitbarDeviceList = [
    {"platformName": "Android", "deviceName": "Dell Venue 8 7840 US"},
    {"platformName": "Android", "deviceName": "Google Pixel 3 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 3 XL -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 3a -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 3a Android 10 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 3a XL -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 3a XL Android 10 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 4 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 4 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 4 XL -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 5 Android 11 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 5 Android 12 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 6 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 6 Android 13 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 6 Pro 5G -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 7 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 7 -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 7 Pro -US"},
    {"platformName": "Android", "deviceName": "Google Pixel 7 Pro Android 13 -US"},
    {"platformName": "Android", "deviceName": "Motorola Moto G Power (2021) -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy A52 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy A52 Android 12 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy J3 Luna Pro -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy J7 Prime SM-J727T1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy Note 10 SM-N970F -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy Note 20 SM-N981U1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy Note 20 SM-N981U1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy Note 20 SM-N981U1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy Note 8 SM-N950U -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S10 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S20 Ultra -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S20 Ultra -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S21 FE 5G -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S22 SM-S901U1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S22 Ultra -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S22 Ultra -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S22 Ultra SM-S908U1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S22+ SM-S906U1 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S23 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S23 Ultra -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S23+ -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S8 -US"},
    {"platformName": "Android", "deviceName": "Samsung Galaxy S9 9.0 -US"},
    {"platformName": "Android", "deviceName": "Samsung SM-J737A 8.0 -US"},
    {"platformName": "Android", "deviceName": "Samsung SM-J737A 9.0 -US"},
    {"platformName": "Android", "deviceName": "Xiaomi Mi A1 -US"}
]

magnetList = [
    "magnet:?xt=urn:btih:6930a566115d2b4811f642da231007fb724f2262",
    "magnet:?xt=urn:btih:7b7fcd3b0fdba2af87a1d0c2c7b4358d57ad774c",
    "magnet:?xt=urn:btih:5f22103e9b2e2dd0a1c43acfb1d1c6aee5f32ad5",
    "magnet:?xt=urn:btih:d50043e3f50010aa85d722af434229da26b4372c",
    "magnet:?xt=urn:btih:9395a4b1a1057d06f206d0f7b33e49e44ca8f702",
    "magnet:?xt=urn:btih:15e5c3c21fc9ff3eea3b6eda7c858b1f87ff9e59",
    "magnet:?xt=urn:btih:867710cacc95ff665132a0ccde2477cc22092d24",
    "magnet:?xt=urn:btih:ad3c11f3f98a966439ddc4f2f92da51afb9ae72b",
    "magnet:?xt=urn:btih:aad07c49c834e08c479a502b51975e6570f7538e",
    "magnet:?xt=urn:btih:6286b7310f87b62b13a5a4a50a01b6fa539af048",
    "magnet:?xt=urn:btih:f495ae7a4b21bb2e79b55aface32d677c2ec9bf1",
    "magnet:?xt=urn:btih:7cf7d92677b5cf09cc81e8aa898c03d4fba9b61e",
    "magnet:?xt=urn:btih:ab74958ee3287ebe73849099c4d540af558dd0e6",
    "magnet:?xt=urn:btih:11ccafbb3d95086dab2afe3f5bc35382c3f7da88",
    "magnet:?xt=urn:btih:c460103d0aeab6f855d8adc309760865dcd96678",
    "magnet:?xt=urn:btih:9a52c116672f478f24fa28353c61f7f79dc90573",
    "magnet:?xt=urn:btih:6683617ef70b3a2769505f0a6c70e9d04e22f6db",
    "magnet:?xt=urn:btih:9d645223cca4c80b56925064a81264d7aed4fa7e",
    "magnet:?xt=urn:btih:1eeb653a476e23551008a9a83966ea23f9ae4a31",
    "magnet:?xt=urn:btih:59f171613ca0d8e326efc134cb5a865e318bf756",
    "magnet:?xt=urn:btih:a0860483beb2d3b8d20eb04d19804153c1984529",
    "magnet:?xt=urn:btih:5e745883e5e3c73b71282751be9e05a6c419ad90",
    "magnet:?xt=urn:btih:7e4d8bbf45364c7db70ad5de366e43cf1203734a",
    "magnet:?xt=urn:btih:7d718bbb75f9d2368658878882411e520d42e485",
    "magnet:?xt=urn:btih:ae3cd89c76804abfeb8977318afdc240de2ef246",
    "magnet:?xt=urn:btih:d2e2b4974ce3340fc06dad26bc0b66b792fce870",
    "magnet:?xt=urn:btih:80d0b723255a721d2576563d4d871471764b6fa2",
    "magnet:?xt=urn:btih:081caaa32361ffc416503b03245fac3080422441",
    "magnet:?xt=urn:btih:ae1dac49c2ddbfbcd061a1393f6051b3dbcbb318",
    "magnet:?xt=urn:btih:70faf0651ca4b6fa90a7b1eee8746f24a7d9b657",
    "magnet:?xt=urn:btih:f855359bd27f0fcba5f45878c1390a3ce31c8e5f",
    "magnet:?xt=urn:btih:494007bfa520ce1cde915be1b69c5c8907c7f8c0",
    "magnet:?xt=urn:btih:2b696583880682f94cce5d3716a5f3bd0958b9fa",
    "magnet:?xt=urn:btih:3f31fb061b8d9d8a9d8758caede7d4c419cbaedf",
    "magnet:?xt=urn:btih:09607f646e0213a331d9e1306fc747f47b0055b8",
    "magnet:?xt=urn:btih:07304eb28206276f1ed5d4d5d87e2f2adca87341",
    "magnet:?xt=urn:btih:09b82e21a46a77944fed0fd68221729f8dc6234d",
    "magnet:?xt=urn:btih:42f4606f617416a9591740bf86ef1c760042f140",
    "magnet:?xt=urn:btih:da35d00c14abc1d934bbb9dad1b590a66e8408fb",
    "magnet:?xt=urn:btih:507cbcf534fbec623af57c72bfab52edc64cbdec",
    "magnet:?xt=urn:btih:8e46dfc80bc344ef20176879d57cec7307998e25",
    "magnet:?xt=urn:btih:e037d954d860a5d90bcd317efec922e2b9fea1b8",
    "magnet:?xt=urn:btih:42087d38b0cce94ca856db48c5f5fdcc874d1aa0",
    "magnet:?xt=urn:btih:f2861cb7689f43d413f264edfa66323d2dbcc5b4",
    "magnet:?xt=urn:btih:0219715f5db04f7bce5ea2a3f17b73ece9bdfada",
    "magnet:?xt=urn:btih:99cb45994245c07a3821917021930f7e6e5aae41",
    "magnet:?xt=urn:btih:0cd2cc21a29b10ec32234b08e5cc5dee96267fbf",
    "magnet:?xt=urn:btih:f734a255c9a2ca85e656a0c88b92a81afb1961b1",
    "magnet:?xt=urn:btih:d8e9cf78fa2f3199af0962cfff2d88f221c45e43",
    "magnet:?xt=urn:btih:3308f22f2a34176d7bc6d5c8151fe9a86fa47efe",
    "magnet:?xt=urn:btih:420fed4e4877a3f57d8fdb6ae803f17007da01ee",
    "magnet:?xt=urn:btih:7d2e9a91da4c5944f06a084c4df5fc161a629795",
    "magnet:?xt=urn:btih:53b0ef405b38a3b0c40c112e9ecfcb3294ae0a6e",
    "magnet:?xt=urn:btih:5f85226c725d4e4de27f1e75f816886b27214c52",
    "magnet:?xt=urn:btih:de0b776de75ca2e2768a9d3c0054c866a3b55cda",
    "magnet:?xt=urn:btih:2e680e9f08d61e17ff87b9f10be5531f49bb7f29",
    "magnet:?xt=urn:btih:4e1e7c845c7f8c1b814876084adc6bfc6cf089ee",
    "magnet:?xt=urn:btih:ad34bfef1eaa44fc1785d0e031fcb9a5776e61d0",
    "magnet:?xt=urn:btih:9c11fecde5c5e7b211f21778e77324968529437a",
    "magnet:?xt=urn:btih:8f67a2fe2dcb54c388131526aa5dd409a2278e21",
    "magnet:?xt=urn:btih:967b3f161f337bfe891507aada27a0ab3817bd6c",
    "magnet:?xt=urn:btih:12da31321ae53d3cea5a0927d41eba56b5135218",
    "magnet:?xt=urn:btih:4413634b13f4fc1330253459080a603cdcf65b12",
    "magnet:?xt=urn:btih:c2e8a411f90ea70890aa652e9d7b1871506de7ed",
    "magnet:?xt=urn:btih:022ba54244d0bee747a05771e9b44c8fcab37bf6",
    "magnet:?xt=urn:btih:6faecc712fab28e013284f352640e1602d6c2089",
    "magnet:?xt=urn:btih:7f2b40037076456fd6bd0d7ca946d0c3668cecda",
    "magnet:?xt=urn:btih:f33671d92c38874d84ae99acd5ed4928bc42c695",
    "magnet:?xt=urn:btih:5b71a1d552f3a4755dcfc9f0f8c2a4b71e94b740",
    "magnet:?xt=urn:btih:13e03bbc83077e663501302fd46ca13eb9fc71e7",
    "magnet:?xt=urn:btih:d3080093cbb531dfbee3df24d5e154fe9a500442",
    "magnet:?xt=urn:btih:6280b62f67277cdc7c001a0d07cc1605b3382f27",
    "magnet:?xt=urn:btih:4fff19f7d7e30b2fbcd470ed2dc361e16c8324b6",
    "magnet:?xt=urn:btih:08e7cc48681ad4031d8d51cedf74a0616716a59a",
    "magnet:?xt=urn:btih:bae74cc8b8468b36469e83d7b6a4c8447258d8f7",
    "magnet:?xt=urn:btih:e67f422f858b81647ac6dd2dbe0ebdfdc5a1a6a6",
    "magnet:?xt=urn:btih:bc0d8c71bc3eed9d0ea56ee1c93825ad97ba838b",
    "magnet:?xt=urn:btih:0df88dcf9a5f178f9d1dc1a99b10b6733f54844f",
    "magnet:?xt=urn:btih:c40fc7a077793d2bf649ed6ce6b976295a84e6e1",
    "magnet:?xt=urn:btih:bd0aa2eaf3333b1333660c9452d02c7d8e9b72ae",
    "magnet:?xt=urn:btih:6d821f6a962c02315473619f39c0edb1ffe2d1f1",
    "magnet:?xt=urn:btih:9d1b45d326bad3b0b527efd838d968f01b96cf15",
    "magnet:?xt=urn:btih:58dd21c6a80137a267f9097ccccffd5257dfe5f0",
    "magnet:?xt=urn:btih:d6f1f34bf72253582b9c07cf1eabea2e3891da1d",
    "magnet:?xt=urn:btih:a4c820fc3c460114381f2d0773f9b540ce88a073",
    "magnet:?xt=urn:btih:628c94aa2e03bbd743333a7c85fa2f7e5e479beb",
    "magnet:?xt=urn:btih:974b531045753a720ccf6deaf695b4d9f68a0525",
    "magnet:?xt=urn:btih:30e566ee320e0f5a903e272eaa9c0c363a72ad69",
    "magnet:?xt=urn:btih:155cec978c7c1b28aea76aabc2787af946319ee3",
    "magnet:?xt=urn:btih:1e27e9a3852b3ccdf7525e8d202d673346b7b698",
    "magnet:?xt=urn:btih:d22533f3a9f99b7c7af29d7d0560861ef95bf1ca",
    "magnet:?xt=urn:btih:2462ba0d7374ba9711d147a98339e60b9510734e",
    "magnet:?xt=urn:btih:e78261e17e600c31c35f91698cd9e0b25c708a33",
    "magnet:?xt=urn:btih:2df23b120737eb0d2aa23a4d8d086868b6da78fa",
    "magnet:?xt=urn:btih:fa9fd0304a5e302ef9b8d7bf56c5ffecbefd67d3",
    "magnet:?xt=urn:btih:aa64644c27a1612e58582a1f7429785ef3c9847c",
    "magnet:?xt=urn:btih:975c4f5e566c418fad0f9a064fa74d91edb7ecc9",
    "magnet:?xt=urn:btih:968c27d45460560d1b0fc46f70ef0f195e8d78b5",
    "magnet:?xt=urn:btih:93d9c58cc14e0d226f946e7f50e9cc20680c18b4",
    "magnet:?xt=urn:btih:cc2950ee4b79605a52d8c0fc8ee5971d2be800a5",
    "magnet:?xt=urn:btih:f6ea134c2bba486dcd28b4f979a5c682cf088407",
    "magnet:?xt=urn:btih:6fbcd0b6b657d275c8331cad718db32a003c004b",
    "magnet:?xt=urn:btih:5dfd9fb4849db7c382d871d2fa7b68f364ec0010",
    "magnet:?xt=urn:btih:ea7c27a5e0728b9f7735ddd4e5c1f8f0ac077f04",
    "magnet:?xt=urn:btih:44cafe1f97f4a6a9a3c450547551e85a7f0c578b",
    "magnet:?xt=urn:btih:a3a61265eacd99ae0c2ce74c5f3bb6550e70d0b4",
    "magnet:?xt=urn:btih:1998dac6ef230b069943debed6f947fedacd96a5",
    "magnet:?xt=urn:btih:ac67b68229667b12209c4b6f3e7dc075626b7bc6",
    "magnet:?xt=urn:btih:1dc7a6c56852e246c457d438e7e4090307d1738f",
    "magnet:?xt=urn:btih:91ab573118ff443390ca8a275b1341eb01d4770e",
    "magnet:?xt=urn:btih:cf40c67ede50c3662b861ad77bb30eab64a4de57",
    "magnet:?xt=urn:btih:24ef843b7a4b5450ad9a7ce3279671e2418a70fc",
    "magnet:?xt=urn:btih:41b88d46cd92a80d3cc66e0d0ed582023bcd9640",
    "magnet:?xt=urn:btih:c09d42886c3e979b3934e45e0e6cbcbdf2c4a410",
    "magnet:?xt=urn:btih:3c1dd506c80d6cd1c222b2ad1dc607946241f18d",
    "magnet:?xt=urn:btih:12d92dab432b009c4837caaaac936496955ece26",
    "magnet:?xt=urn:btih:82b24be8318aaa30687b7d4d10889daf6f0cd527",
    "magnet:?xt=urn:btih:dd402f4eb85adb1b4f85e2b3358c3c2f353ade79",
    "magnet:?xt=urn:btih:565fbe81b6d4af1c9ec55fd28ac325947881a8ba",
    "magnet:?xt=urn:btih:a9319265255f8f6eff0cade0a231b52c8dda6e94",
    "magnet:?xt=urn:btih:f3013cbc1de7c27e169f9362690c4ec0d0c85be8",
    "magnet:?xt=urn:btih:7421296428f84ba3e144ef85db158c06276a3cad",
    "magnet:?xt=urn:btih:3b1e9640cc369fa8c9c1d274acf1207ffdd56845",
    "magnet:?xt=urn:btih:35aec715b1306917c9f6a6f3ee433a3f9f9e1e05",
    "magnet:?xt=urn:btih:d0a3f7432a7d9e4fd8b2727914f3b8fdc4e6b32e",
    "magnet:?xt=urn:btih:2b0464e277324c0541e90f763077947f27fc48c3",
    "magnet:?xt=urn:btih:63485f45c6791ed819e0f9f3c0652d06f3455db8",
    "magnet:?xt=urn:btih:cc98e515391c62e14bae463d4146c77595924ce9",
    "magnet:?xt=urn:btih:9b8c56277d858639ffc4f6d09bc967c0d11fd39f",
    "magnet:?xt=urn:btih:88a96ed82289560e56a72760848909bea568b37a",
    "magnet:?xt=urn:btih:a17f4c9cec27ed0f205143ce33eb4d4c0152cbfd",
    "magnet:?xt=urn:btih:0702a8c24a72b08bda73f06ce93a2905aea37562",
    "magnet:?xt=urn:btih:530f9a901b33c554fbf68d9886b84aa26568ac48",
    "magnet:?xt=urn:btih:814d10b4c2ca7c731eead11917bf7ab8b6268ba0",
    "magnet:?xt=urn:btih:def98f74561972904589a0448158794ccdaf2550",
    "magnet:?xt=urn:btih:f6078cdb09453e23f55a1da0f564490a5a942dbe"
]

userList = ["#user#"]
passwordList = ["#password#"]
testPlatform = "#testPlatform#" # testingbot bitbar samsung appetize


highVersionAppium = True
downloadApk = True

waitTime = 10

#appDownloadUrl = "https://www.pastefile.com/download/6nadk9"

#appDownloadUrl = "https://up.mediy.cn/PikPak-v1_b26c11f0a3bea7ee6506cd468a411201.apk"
appDownloadUrl = "https://d.kstore.space/download/7536/PikPak-v1.42.6.apk"
#appDownloadUrl = "https://github.com/hhsw2015/appium-test/raw/main/PikPak-v1.42.6.apk"


appLocalUrl = os.getcwd() + "/PikPak-v1.42.6.apk"


deviceIP = 'localhost:56238'
#deviceIP = 'localhost:6000'

testingbotKeySecretList = [{"key" : "1a0bf178195c4e36e2efa0b5949e6038", "secret" : "4dd916da06c59a866634845f03aa0a8c"}]
bitbarKeyList = ["Dq36i2kaMcale4sRflBY9G4l2GxAAttt"]

def getTestPlatformArgs(testPlatform, highVersionAppium=True, appDownloadUrl='', deviceIP="", apiKey='', secret="", userName=''):
    print("getTestPlatformArgs for " + testPlatform)
    device = {}
    desired_caps = {}
    url = ""

    #key = os.environ['key']
    #secret = os.environ['secret']

    appPackage = "com.pikcloud.pikpak"
    appActivity = "com.pikcloud.app.SplashActivity"


    if testPlatform == "testingbot":
        '''
        device = {
            "platformName": "Android",
            "deviceName": "Galaxy S8",
            "version": "9.0"
        }
        '''

        device = random.choice(testingbotDeviceList)


        keySecretDict = random.choice(testingbotKeySecretList)

        if apiKey == "":
            apiKey = keySecretDict["key"]
        if secret == "":
            secret = keySecretDict["secret"]
        url = "http://" + apiKey + ":" + secret + "@hub.testingbot.com/wd/hub" #testingbot

        desired_caps = {
            "deviceName": device["deviceName"],
            "platformName": device["platformName"],
            "version" : device["version"],
            "app": appDownloadUrl,
            "realDevice": True
        }

    elif testPlatform == "samsung":
        #deviceIP = "localhost:56238" # https://developer.samsung.com/remotetestlab/devices

        device = {
                "platformName": "Android",
                "deviceName": deviceIP,
                "uuid": deviceIP,
                "version": "14"
        }

        desired_caps = {
            "deviceName": device["deviceName"],
            "platformName": device["platformName"],
            "version": device["version"],
            "app": appDownloadUrl,
            "realDevice": True,
            "uiautomator2ServerInstallTimeout": 60000,
            "androidInstallTimeout": 200000,
            "appPackage": appPackage,
            "appActivity": appActivity
        }


    elif testPlatform == "appetize":
        #deviceIP = "localhost:6000" #https://appetize.io

        device = {
                "platformName": "Android",
                "deviceName": deviceIP,
                "uuid": deviceIP,
                "version": "14"
        }

        desired_caps = {
            "deviceName": device["deviceName"],
            "platformName": device["platformName"],
            "version": device["version"],
            "app": appDownloadUrl,
            "realDevice": True,
            "uiautomator2ServerInstallTimeout": 60000,
            "androidInstallTimeout": 200000,
            "appPackage": appPackage,
            "appActivity": appActivity
        }

    elif testPlatform == "bitbar":

        #url = "https://eu-mobile-hub.bitbar.com/wd/hub"

        #url = "https://us-west-mobile-hub.bitbar.com/wd/hub"

        url = random.choice(['https://eu-mobile-hub.bitbar.com/wd/hub','https://us-west-mobile-hub.bitbar.com/wd/hub'])
        '''
        desired_caps = {
        'platformName': 'Android',
        'appium:automationName': 'uiautomator2',
        'bitbar:options': {
            'project': 'pp',
            'testrun': 'test',
            'app': '217003986',
            'apiKey': 'p1yIHSngRIGTGGiCY14362o6TfFbZCVH',
            'device': 'Google Pixel 3a Android 12',
            'appiumVersion': '2.1',
            "appPackage": appPackage,
            "appActivity": appActivity
            }
        }
        '''

        device = random.choice(bitbarDeviceList)

        if apiKey == "":
            apiKey = random.choice(bitbarKeyList)

        desired_caps = {
            'platformName': device["platformName"],
            'appium:automationName': 'uiautomator2',
            'bitbar:options': {
                'app': appDownloadUrl,
                'apiKey': apiKey,
                'device': device["deviceName"],
                'appiumVersion': '2.1',
                "appPackage": appPackage,
                "appActivity": appActivity
            }
        }
    elif testPlatform == "saucelabs":
        #https://docs.saucelabs.com/mobile-apps/automated-testing/appium/real-devices/
        #https://docs.saucelabs.com/mobile-apps/automated-testing/appium/configuration/
        desired_caps = {
            'platformName': "Android",
            'appium:automationName': 'uiautomator2',
            'appium:orientation': 'portrait',
            'app': appDownloadUrl,
            'appPackage': appPackage,
            'appActivity': appActivity,
            'sauce:options': {
                'username': userName,
                'accessKey': apiKey
            }
        }

        url = "http://" + userName + ":" + apiKey + "@ondemand.us-west-1.saucelabs.com/wd/hub"
    elif testPlatform == "browserstack":
        #https://github.com/browserstack/python-appium-app-browserstack/blob/master/android/browserstack_sample.py
        #https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started
        
        dList = ["Google", "Samsung", "OnePlus", "Oppo", "Xiaomi", "Vivo", "Motorola", "Huawei", "Realme"]
        desired_caps = {
            # Specify device and os_version for testing
            "platformName" : "android",
            "platformVersion" : "1[01234]",
            "deviceName" : random.choice(dList) + ".*",
            # Set URL of the application under test
            "app" : appDownloadUrl,
            # Set other BrowserStack capabilities
            'bstack:options' : {
                #"projectName" : "First Python project",
                #"buildName" : "browserstack-build-1",
                #"sessionName" : "BStack first_test",
                # Set your access credentials
                "userName" : userName,
                "accessKey" : apiKey
            }
        }

        url = "http://hub.browserstack.com/wd/hub"
    elif testPlatform == "applitools":
        #https://applitools.com/tutorials/quickstart/native-mobile/appium/python
        print("applitools")
    elif testPlatform == "mumuplayer":
        #deviceIP = "127.0.0.1:16384" #https://appetize.io

        device = {
                "platformName": "Android",
                "deviceName": deviceIP,
                "uuid": deviceIP,
                "version": "12"
        }

        desired_caps = {
            "deviceName": device["deviceName"],
            "platformName": device["platformName"],
            "version": device["version"],
            "app": appLocalUrl,
            "realDevice": True,
            "uiautomator2ServerInstallTimeout": 60000,
            "androidInstallTimeout": 200000,
            "appPackage": appPackage,
            "appActivity": appActivity
        }

        url = "http://127.0.0.1:4723" #2.5.0


    

    print(device)

    print(desired_caps)

    if url == "":
        if highVersionAppium:
            url = "http://127.0.0.1:4723" #2.5.0
        else:

            url = "http://127.0.0.1:4723/wd/hub" #1.22.0

    print(url)

    return url, desired_caps


def runTask(user, password, url, desired_caps, waitTime=10):
    options = UiAutomator2Options().load_capabilities(desired_caps)

    print("connect to " + url)
    error = False
    driver = None
    try:
        driver = webdriver.Remote(url, options=options)
    except Exception as e:
        print(e)
        error = True
        return error

    try:

        print("do task for " + user)


        print("login ...")
        #com.pikcloud.pikpak:id/iv_email_login
        print("start login ...")

        inputA = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.pikcloud.pikpak:id/iv_email_login")))
        inputA.click()

        print("input user name ...")

        inputB = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.pikcloud.pikpak:id/et_email")))
        inputB.send_keys(user)

        print("input password ...")

        inputB = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.pikcloud.pikpak:id/et_password")))
        inputB.send_keys(password)

        if driver.is_keyboard_shown():
            driver.hide_keyboard()

        print("click login ...")

        inputB = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.pikcloud.pikpak:id/tv_login")))
        inputB.click()

        #inputB = WebDriverWait(driver, 30).until(
        #    EC.element_to_be_clickable((AppiumBy.ID, "com.pikcloud.pikpak:id/iv_close"))
        #)
        #inputB.click()

        #inputB = WebDriverWait(driver, 30).until(
        #    EC.element_to_be_clickable((AppiumBy.ID, "com.pikcloud.pikpak:id/close"))
        #)
        #inputB.click()

        #inputB = WebDriverWait(driver, 30).until(
        #    EC.element_to_be_clickable((AppiumBy.ID, "com.pikcloud.pikpak:id/bg_image_view"))
        #)
        #inputB.click()

        random_num = random.randint(1, 3)

        print("download magnet ...")


        for i in range(random_num):
            print("click add ...")

            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/add_button")))
            inputB.click()

            print("click add to cloud...")

            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/add_to_cloud")))
            inputB.click()

            print("input magnet link...")

            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/input")))
            magnetLink = random.choice(magnetList)
            inputB.send_keys(magnetLink)

            print("downloading " + magnetLink)

            if driver.is_keyboard_shown():
                driver.hide_keyboard()

            print("start download magnet link...")

            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/add")))
            inputB.click()


        print("play video ...")

        print("click conver image...")

        inputB = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.pikcloud.pikpak:id/cover_image")))
        inputB.click()

        #com.pikcloud.pikpak:id/tv_download_continue

        try:
            print("click continue..")
            inputB = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID,
                     "com.pikcloud.pikpak:id/tv_download_continue")))
            if inputB != None:
                inputB.click()
        except:
            print("no tv_download_continue button")

        try:
            print("click next button..")
            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/next_button")))
            inputB.click()

            print("click next button..")
            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/next_button")))
            inputB.click()

            print("click next button..")
            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/next_button")))
            inputB.click()

            print("click next button..")
            inputB = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.pikcloud.pikpak:id/next_button")))
            inputB.click()
        except:
            print("click next error")


        print("sleep for " + str(waitTime) + " seconds")
        time.sleep(waitTime)

        print("finshed " + user)
    except:
        print("error and quit")
        error = True
    finally:
        print("driver quit")
        driver.quit()

    return error





def main(argv):
    global userList, passwordList, testPlatform, waitTime, appDownloadUrl, deviceIP
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:p:t:k:s:n:w:a:i:r:h', ["user", "password", "testPlatform", "key", "secret", "name","waitTime", "apkPath", "ip", "retry", "help"])
    except getopt.GetoptError as err:
        sys.exit(2)

    apiKey = ""
    secret = ""
    name=''
    retry = 0

    if os.path.exists("bitbar_key.txt"):
        bitbarKeyList = []
        with open("bitbar_key.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().replace("\n", "")
                if line != "" and line.startswith("#") == False:
                    bitbarKeyList.append(line)

    if os.path.exists("testingbot_key_secret.txt"):
        testingbotKeySecretList = []
        with open("testingbot_key_secret.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().replace("\n", "")

                if line != "" and line.startswith("#") == False:
                    items = line.split(" ")
                    testingbotKeySecretList.append({"key" : items[0], "secret" : items[1]})

    for o, a in opts:
        if o in ('-u', '--user'):
            if a.find(",") != -1:
                userList = a.split(",")
            else:
                userList = [a]
        elif o in ('-p', '--password'):
            if a.find(",") != -1:
                passwordList = a.split(",")
            else:
                passwordList = [a]
        elif o in ('-k', '--key'):
            apiKey = str(a)
        elif o in ('-s', '--secret'):
            secret = str(a)
        elif o in ('-n', '--name'):
            name = str(a)
        elif o in ('-t', '--testPlatform'):
            testPlatform = str(a)
        elif o in ('-w', '--waitTime'):
            waitTime = int(a)
        elif o in ('-a', '--apkPath'):
            appDownloadUrl = str(a)
        elif o in ('-i', '--ip'):
            deviceIP = str(a)
        elif o in ('-r', '--retry'):
            retry = int(a)
        elif o in ('-h', '--help'):
            print("./test.py -u user -p password -t testingbot -w 10 -k apiKey -s secret")
            print("./test.py -u user -p password -t bitbar -w 10 -k apiKey")
            print("./test.py -u user -p password -t samsung -a /home/ubuntu/workspace/PikPak-v1.42.6.apk -w 10 -i localhost:56238")
            print("./test.py -u user -p password -t appetize -a /home/ubuntu/workspace/PikPak-v1.42.6.apk -w 10 -i localhost:6000")
            print("./test.py -u user -p password -t saucelabs -w 10 -n name -k apiKey")
            print("./test.py -u user -p password -t browserstack -w 10 -n name -k apiKey")
            print("./test.py -u user -p password -t mumuplayer -w 10 -i 127.0.0.1:16384")


            if testPlatform == "testingbot":
                print(" ")
                for item in testingbotKeySecretList:
                    for i in range(len(userList)):
                        u = userList[i]
                        p = passwordList[i]
                        print("./test.py -u " + u + " -p " + p + " -t testingbot -w " + str(waitTime) + " -k " + item["key"] + " -s " + item["secret"])
            elif testPlatform == "bitbar":
                print(" ")
                for key in bitbarKeyList:
                    for i in range(len(userList)):
                        u = userList[i]
                        p = passwordList[i]
                        print("./test.py -u " + u + " -p " + p + " -t bitbar -w " + str(waitTime) + " -k " + key)
            
            sys.exit()


    print(userList)
    print(passwordList)
    print(apiKey)
    print(str(waitTime))
    print(testPlatform)

    #sys.exit()

    for i in range(len(userList)):
        user = userList[i].strip()
        password = passwordList[i].strip()

        if user != "" and password!= "":
            error = False
            while retry >= 0:
                url, desired_caps = getTestPlatformArgs(testPlatform, highVersionAppium=highVersionAppium, appDownloadUrl=appDownloadUrl, deviceIP=deviceIP, apiKey=apiKey, secret=secret, userName=name)
                error = runTask(user, password, url, desired_caps, waitTime=waitTime)

                if error == False:
                    break
                else:                 
                    if retry <= 0:
                        break
                    retry -= 1


if __name__ == '__main__':
    main(sys.argv)

