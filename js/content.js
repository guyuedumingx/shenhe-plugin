// document.addEventListener('mousedown', (event) => {
//     if (event.button === 1) { // 鼠标中键
//         // chrome.runtime.sendMessage({ type: 'middleClick' });
//         console.log("click middle mouse button")
//         if (event.button === 1) {
//             event.preventDefault(); // 防止默认的中键行为（如打开新标签）

//             // 查找 ID 为 'submit' 的按钮
//             const submitButton = document.getElementById('submit');
//             if (submitButton) {
//                 submitButton.click(); // 触发按钮的点击事件
//             }
//         }
//     }
// });

document.addEventListener('dblclick', (event) => {
    if (event.button === 1) { 
        console.log("double click middle mouse button")
        // 防止默认的中键行为（如打开新标签）
        event.preventDefault(); 

        const submitButton = document.getElementById('submit');
        if (submitButton) {
            submitButton.click();
        }

        // 创建一个观察器实例并传入回调函数
        const observer = new MutationObserver((mutations, obs) => {
            const floatingWindow = document.getElementById('your-floating-window-id'); // 替换为悬浮窗的实际 ID
            if (floatingWindow) {
                // 检测到悬浮窗
                // 定位到悬浮窗中的按钮并点击
                const submitActionBtn = floatingWindow.querySelector('#submit_action');
                if (submitActionBtn) {
                    submitActionBtn.click();
                    obs.disconnect();
                }
            }
        });

        // 配置观察器的选项
        const config = { childList: true, subtree: true };

        // 启动观察器
        observer.observe(document.body, config);
    }
});

chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        res = ""
        if (request.action === "all_img_tag_src") res = all_img_tag_src()
        sendResponse(res);
    }
);

/**
 * send all img tag src as a list to background
 */
var all_img_tag_src = () => {
    var images = document.querySelectorAll('img');
    var imgs = Array.from(images).filter(img => img.src.length > 50);
    return imgs.map(img => img.src);
}