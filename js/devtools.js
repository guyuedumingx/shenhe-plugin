  chrome.devtools.network.onRequestFinished.addListener(function(request) {
    // if (request.response.bodySize > 10 * 1024 && request.request.url.endsWith('.jpg')) {
    if (request.response.bodySize > 10 * 1024) {
      // 发送请求到你的Python后端
      fetch("http://localhost:8889/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ largeImages: request.request.url })
      });
    }
  });
