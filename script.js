/* موسوعة اليوم — تفاعلات عامة */
document.addEventListener('DOMContentLoaded', function () {

  // FAQ Accordion
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      q.parentElement.classList.toggle('open');
    });
  });

  // تفعيل روابط CTA من الإعدادات (احتياطي إن لم يُستبدل النص)
  if (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.targetUrl.indexOf('TARGET-SITE') === -1) {
    document.querySelectorAll('a[data-target-cta]').forEach(function (a) {
      if (a.getAttribute('href').indexOf('TARGET-SITE') !== -1) {
        a.href = SITE_CONFIG.targetUrl;
      }
    });
  }

  // سنة الحقوق
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
});
