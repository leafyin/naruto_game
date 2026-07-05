// script.js
// 通过接口获取下拉框内容
async function loadDropdown() {
    const response = await fetch('http://localhost:9547/dropdown');
    const data = await response.json(); // 假设返回的格式是字符串数组
    const dropdown = document.getElementById('dropdown');

    // 清空下拉框
    dropdown.innerHTML = '';
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    defaultOption.textContent = '请选择设备';
    dropdown.appendChild(defaultOption);

    data.forEach(item => {
        const option = document.createElement('option');
        option.value = item; // 设置option的值
        option.textContent = item; // 设置option的文本
        dropdown.appendChild(option);
    });
}

// 下拉框改变事件处理
function handleDropdownChange() {
    const dropdown = document.getElementById('dropdown');
    const selectedValue = dropdown.value;

    // 如果选择了设备，则调用 selectDevice 接口
    if (selectedValue) {
        selectDevice(selectedValue);
    }
}

// 调用 selectDevice 接口
async function selectDevice(device) {
    const response = await fetch(`http://localhost:9547/selectDevice/${device}`);
    if (response.ok) {
        console.log(`成功选择设备: ${device}`);
        // 可以在这里添加更多的操作，例如更新界面等
    } else {
        console.error(`选择设备失败: ${device}`);
    }
}

// 监听下拉框展开事件
document.getElementById('dropdown').addEventListener('focus', loadDropdown);

// 监听下拉框变化
document.getElementById('dropdown').addEventListener('change', handleDropdownChange);

function handleClick(item, index, button) {
    // 获取所有按钮并置灰
    const allButtons = document.querySelectorAll('button');
    allButtons.forEach(btn => {
        btn.disabled = true; // 禁用所有按钮
    });

    // 获取当前点击按钮旁边的进度条
    const progressCircle = button.nextElementSibling;
    const progressBar = progressCircle.querySelector('.progress-fg');

    // 显示进度条
    progressCircle.style.display = 'inline-block';
    let progress = 0;
    progressBar.style.strokeDashoffset = '100';

    // 创建一个XMLHttpRequest对象
    const xhr = new XMLHttpRequest();

    // 设置请求地址和方式
    const url = `http://localhost:9547/action/${index}`;
    xhr.open("GET", url, true);

    // 模拟缓慢增长动画
    const progressInterval = setInterval(() => {
        if (progress < 80) {
            progress += 1;
            const offset = 100 - (progress * 100 / 100);
            progressBar.style.strokeDashoffset = offset;
        }
    }, 100);  // 每100ms增加1%

    // 请求状态监听
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            clearInterval(progressInterval);  // 停止模拟进度
            progress = 100;
            const offset = 100 - (progress * 100 / 100);
            progressBar.style.strokeDashoffset = offset;

            // 延迟0.5秒后隐藏进度条并复原按钮
            setTimeout(() => {
                progressCircle.style.display = 'none'; // 隐藏进度条
                allButtons.forEach(btn => {
                    btn.disabled = false; // 复原按钮
                });

                // 根据请求结果更新记录区域
                const recordSection = document.getElementById('recordSection');
                const recordItem = document.createElement('div');
                recordItem.className = 'record-item ' + (xhr.status === 200 ? 'success' : 'failure');
                recordItem.textContent = `${item} ${xhr.status === 200 ? '成功' : '失败'}`;
                recordSection.appendChild(recordItem);
            }, 500); // 延迟500ms
        }
    };

    // 发送请求
    xhr.send();
}
