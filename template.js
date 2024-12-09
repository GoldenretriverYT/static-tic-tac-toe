function preloadLinks() {
  const links = document.querySelectorAll("a");
  links.forEach(async (link) => {
    const originalHref = link.href;
    const pageRequest = await fetch(link.href);
    const pageText = await pageRequest.text();
    link.setAttribute("href", "#");
    
    link.addEventListener("click", (event) => {
      document.body.innerHTML = pageText;
      window.history.pushState({}, "", originalHref);
      preloadLinks();
      
      event.preventDefault();
      return false;
    });
  });
}

preloadLinks();
