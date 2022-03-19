const menuItems = document.querySelectorAll('[id^=menu-item]')

const menuClick = event => {
  let itemClicked = event.target.className.substring(9, 10)
  let itemInt = parseInt(itemClicked)
  const choice = document.getElementById('choice' + itemInt)

  const menuItems = document.querySelectorAll("[id^=menu-item]")
  menuItems.forEach(item => {
    item.style.backgroundColor = "rgba(0,0,0,0.5)"
  })
  const items = document.querySelectorAll("[id^=item]")
  items.forEach(item => {
    item.style.backgroundColor = "rgba(0,0,0,0)"
  })


  const element = document.getElementById("item" + itemInt)
  element.style.backgroundColor = "rgba(0,0,0,1)";
  element.parentElement.style.backgroundColor = "rgba(0,0,0,1)";

  choice.checked = true
}

menuItems.forEach(item => {
  item.addEventListener('click', menuClick)
  const children = item.childNodes

  children.forEach(child => {
    child.addEventListener('click', menuClick)
  })
})

