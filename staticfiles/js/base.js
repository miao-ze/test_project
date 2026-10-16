// 等待页面DOM完全加载后再执行
document.addEventListener('DOMContentLoaded', function () {
  const goWallBtn = document.getElementById('goWallBtn');

  if (goWallBtn) {
    goWallBtn.addEventListener('click', function () {
      console.log('点击了逛逛表白墙');
      // 用绝对路径跳转，避免相对路径出错
      window.location.href = '/articles/';
    });
  } else {
    // 控制台会打印提示，方便排查
    console.error('未找到id为goWallBtn的按钮，请检查id是否正确');
  }
});