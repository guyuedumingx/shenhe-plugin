function sendData(data) {
    var socket = new WebSocket('ws://localhost:8889');

    socket.onopen = function (event) {
        socket.send(JSON.stringify(data));
    };

    socket.onmessage = function (event) {
        alert("Data received from server: " + event.data);
    };

    socket.onerror = function (event) {
        console.error("WebSocket error observed:", event);
    };
}

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "all_to_gray",
    title: "所有影像转灰度图",
  });
  chrome.contextMenus.create({
    id: "selected_to_gray",
    title: "转灰度图",
    contexts: ["image"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "all_to_gray") {
    (async () => {
      const [tab] = await chrome.tabs.query({active: true, lastFocusedWindow: true});
      const data = await chrome.tabs.sendMessage(tab.id, {action: "all_img_tag_src"});
      sendData({action:"all_to_gray", data:data, args:{}})
    })();
  } else if(info.menuItemId === "selected_to_gray") {
    if (info.srcUrl) {
      sendData({action: "one_to_gray", data:info.srcUrl, args:{}})
    }
  }
});