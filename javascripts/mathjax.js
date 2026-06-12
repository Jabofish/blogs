// docs/javascripts/mathjax.js — MathJax 4.1.x config
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    enableExplorer: true
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise()
})
