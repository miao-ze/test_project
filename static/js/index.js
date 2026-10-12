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



// 移动端菜单切换
const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// 滚动时导航栏样式变化
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
        navbar.classList.add('shadow-md');
        navbar.classList.remove('bg-white/80');
        navbar.classList.add('bg-white/95');
    } else {
        navbar.classList.remove('shadow-md');
        navbar.classList.add('bg-white/80');
        navbar.classList.remove('bg-white/95');
    }
});

// 点赞按钮交互
document.querySelectorAll('.like-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        this.classList.toggle('active');
        const icon = this.querySelector('i');
        const countText = this.childNodes[1];
        let count = parseInt(countText.textContent.trim());

        if (this.classList.contains('active')) {
            icon.classList.remove('fa-regular');
            icon.classList.add('fa-solid');
            countText.textContent = ' ' + (count + 1);
        } else {
            icon.classList.remove('fa-solid');
            icon.classList.add('fa-regular');
            countText.textContent = ' ' + (count - 1);
        }
    });
});

// ========== 登录注册功能 ==========
const authModal = document.getElementById('authModal');
const loginBtn = document.getElementById('loginBtn');
const mobileLoginBtn = document.getElementById('mobileLoginBtn');
const publishBtn = document.getElementById('publishBtn');
const closeModal = document.getElementById('closeModal');
const authTabs = document.querySelectorAll('.auth-tab');
const authForms = document.querySelectorAll('.auth-form');

// 打开模态框
function openAuthModal() {
    authModal.classList.remove('hidden');
    authModal.classList.add('flex');
    document.body.style.overflow = 'hidden';
}

loginBtn.addEventListener('click', openAuthModal);
mobileLoginBtn.addEventListener('click', openAuthModal);
publishBtn.addEventListener('click', openAuthModal); // 未登录时点击发布也打开登录框

// 关闭模态框
function closeAuthModal() {
    authModal.classList.add('hidden');
    authModal.classList.remove('flex');
    document.body.style.overflow = '';
}

closeModal.addEventListener('click', closeAuthModal);

// 点击背景关闭模态框
authModal.addEventListener('click', (e) => {
    if (e.target === authModal) {
        closeAuthModal();
    }
});

// ESC键关闭模态框
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !authModal.classList.contains('hidden')) {
        closeAuthModal();
    }
});

// 登录/注册标签切换
authTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = tab.dataset.tab;

        // 切换标签样式
        authTabs.forEach(t => {
            t.classList.remove('text-primary', 'border-primary');
            t.classList.add('text-gray-500', 'border-transparent');
        });
        tab.classList.remove('text-gray-500', 'border-transparent');
        tab.classList.add('text-primary', 'border-primary');

        // 切换表单
        authForms.forEach(form => {
            form.classList.add('hidden');
        });
        document.getElementById(target + 'Form').classList.remove('hidden');
    });
});

// 密码显示/隐藏切换
document.querySelectorAll('.toggle-pwd').forEach(btn => {
    btn.addEventListener('click', function() {
        const input = this.parentElement.querySelector('input');
        const icon = this.querySelector('i');

        if (input.type === 'password') {
            input.type = 'text';
            icon.classList.remove('fa-regular', 'fa-eye');
            icon.classList.add('fa-regular', 'fa-eye-slash');
        } else {
            input.type = 'password';
            icon.classList.remove('fa-regular', 'fa-eye-slash');
            icon.classList.add('fa-regular', 'fa-eye');
        }
    });
});
