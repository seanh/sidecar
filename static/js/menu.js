// Highlight any menu links to the current page.
for (menu of document.getElementsByClassName('navbar')) {
  for (menuLink of menu.getElementsByTagName('a')) {
    if (menuLink.href === document.URL) {
      menuLink.setAttribute('aria-current', 'page');
    }
  }
}
