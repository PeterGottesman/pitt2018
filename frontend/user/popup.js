// Copyright (c) 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

function getAuthor() {
    var author = "";
    var info = document.getElementsByTagName('META');
    for (var i=0;i<info.length;i++) {
	if (info[i].getAttribute('NAME') && info[i].getAttribute('NAME').toLowerCase()=='author') {
	    author = info[i].getAttribute('CONTENT');
	}
    }
    return author;
}

/**
 * Get the current URL.
 *
 * @param {function(string)} callback called when the URL of the current tab
 *   is found.
 */
function getCurrentTabUrl(callback) {
    // Query filter to be passed to chrome.tabs.query - see
    // https://developer.chrome.com/extensions/tabs#method-query
    var queryInfo = {
	active: true,
	currentWindow: true
    };

    chrome.tabs.query(queryInfo, (tabs) => {
	// chrome.tabs.query invokes the callback with a list of tabs that match the
	// query. When the popup is opened, there is certainly a window and at least
	// one tab, so we can safely assume that |tabs| is a non-empty array.
	// A window can only have one active tab at a time, so the array consists of
	// exactly one tab.
	var tab = tabs[0];

	// A tab is a plain object that provides information about the tab.
	// See https://developer.chrome.com/extensions/tabs#type-Tab
	var url = tab.url;
	callback(url);
    });

    // Most methods of the Chrome extension APIs are asynchronous. This means that
    // you CANNOT do something like this:
    //
    // var url;
    // chrome.tabs.query(queryInfo, (tabs) => {
    //   url = tabs[0].url;
    // });
    // alert(url); // Shows "undefined", because chrome.tabs.query is async.
}

function getReviewsByURLExact(url) {
    var getUrl =  "http://localhost:5000/getReviews/byURL?exact=True&url="+url;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", getUrl, false);
    xhr.send(null);
    displayReviews(xhr.responseText);
}

function getReviewsBySite(url) {
    var getUrl =  "http://localhost:5000/getReviews/byURL?url="+url;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", getUrl, false);
    xhr.send(null);
    displayReviews(xhr.responseText);
}

function getReviewsByAuthor(url, title, author) {
    var getUrl =  "http://localhost:5000/getReviews"
    var xhr = new XMLHttpRequest();
    xhr.open("GET", getUrl, false);
    xhr.send(null);
    displayReviews(xhr.responseText);
}

function displayReviews(json) {
    
}

window.addEventListener('load', function load(event){
    getCurrentTabUrl(getReviewsByURLExact);
});
