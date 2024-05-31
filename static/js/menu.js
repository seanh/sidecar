// Highlight any menu links to the current page.
for (menuLink of document.getElementById('menu').getElementsByTagName('a')) {
  if (menuLink.href === document.URL) {
    menuLink.setAttribute('aria-current', 'page');
  }
}
