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
}

function getReviewsByURLExact(url) {
    var getUrl =  "http://localhost:5000/getReviews/byURL?exact=True&url="+url;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", getUrl, false);
    xhr.send(null);
    var data = xhr.responseText;
    console.log(data);
    displayReviews(JSON.parse(data));
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
    console.log(json);
    document.write("<ul>");
    for (var rating in json["ratings"]) {
	document.write("<li> Rating:" + json["ratings"][rating].rating + " Reviewer: " + json["ratings"][rating].reviewer + " </li>");
    }
    document.write("</ul>");
}

window.addEventListener('load', function load(event){
    getCurrentTabUrl(getReviewsByURLExact);
});
