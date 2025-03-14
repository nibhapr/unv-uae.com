// Scroll Progress Indicator
document.addEventListener('DOMContentLoaded', function() {
  // Create the progress elements
  const progressContainer = document.createElement('div');
  progressContainer.className = 'scroll-progress-container';
  
  const progressBar = document.createElement('div');
  progressBar.className = 'scroll-progress-bar';
  progressBar.id = 'scrollProgressBar';
  
  // Append to the DOM
  progressContainer.appendChild(progressBar);
  document.body.insertBefore(progressContainer, document.body.firstChild);
  
  // Add styles
  const style = document.createElement('style');
  style.textContent = `
    .scroll-progress-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: transparent;
      z-index: 9999;
      pointer-events: none;
    }
    
    .scroll-progress-bar {
      height: 100%;
      width: 0;
      background: var(--primary-color, #3498db);
      transition: width 0.1s ease-out;
      will-change: width;
      transform: translateZ(0);
    }
    
    @media (prefers-reduced-motion: reduce) {
      .scroll-progress-bar {
        transition: none;
      }
    }
  `;
  document.head.appendChild(style);
  
  // Track scroll progress
  let ticking = false;
  
  function updateScrollProgress() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrollPercentage = windowHeight > 0 ? (scrollTop / windowHeight) * 100 : 0;
    
    progressBar.style.width = `${scrollPercentage}%`;
    ticking = false;
  }
  
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        updateScrollProgress();
        ticking = false;
      });
      
      ticking = true;
    }
  }, { passive: true });
  
  // Initial call to set progress bar on page load
  updateScrollProgress();
  
  // Update on resize (debounced for performance)
  let resizeTimeout;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(updateScrollProgress, 100);
  }, { passive: true });
}); 