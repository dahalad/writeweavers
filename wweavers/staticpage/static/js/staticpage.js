function setActive(active_element) {
    current = document.getElementsByClassName('active')[0]
    current.classList.remove('active')
    next = document.getElementById(active_element)
    next.classList.add('active')
}
