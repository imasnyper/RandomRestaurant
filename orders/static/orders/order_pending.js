let timer = 0;

const updateTimer = () => {
  timer += 1;
  let timeLeft = document.getElementById("timeLeft")
  timeLeft.innerText = "Order Ready in: " + (5 - timer).toString();
}

const timerInterval = setInterval(updateTimer, 1000)

const fullfillOrder = async () => {
  let hiddenInput = document.getElementById("DRF_TOKEN")
  const drfToken = hiddenInput.value

  hiddenInput = document.getElementById("ORDER_PK")
  const orderPk = hiddenInput.value

  const dateString = createDateString()

  const requestData = {datetime_fulfilled: dateString}

  const response = await fetch("api/orders/" + orderPk + "/", {
    method: 'PUT',
    headers: {
      'Authorization': 'Token ' + drfToken,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestData)
  })

  const data = await response.json()

  updateUI(data)
  clearInterval(timerInterval)
  const timeLeft = document.getElementById("timeLeft")
  timeLeft.innerText = ""
}

const createDateString = () => {
  const date = new Date()
  let offsetSign;

  let tzOffset = date.getTimezoneOffset();
  if(tzOffset < 0) {
    offsetSign = "+"
    tzOffset = tzOffset / -60
  } else {
    offsetSign = "-"
    tzOffset = tzOffset / 60
  }
  const tzOffsetString = offsetSign + tzOffset.toString().padStart(2, '0') + ':00'

  return date.getFullYear() + "-" +
    (date.getMonth() + 1).toString().padStart(2, '0') + "-" +
    date.getDate().toString().padStart(2, '0') +
    "T" +
    date.getHours().toString().padStart(2, '0') +
    ":" + date.getMinutes().toString().padStart(2, '0') +
    ":" + date.getSeconds().toString().padStart(2, '0') +
    tzOffsetString
}

const updateUI = data => {
  const fulfilled = new Date(data.datetime_fulfilled)
  const dish = data.dish_name
  const orderStatus = document.getElementById("orderStatus")
  orderStatus.innerText = "Order for " + dish + " fulfilled " + fulfilled.toLocaleTimeString()
}

setTimeout(fullfillOrder, 5000)