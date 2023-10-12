from socket import timeout
from pyppeteer import launch

async def get_trello_tasks():
  print("Iniciando sesión en Trello...")
  browser = await launch()
  page = await browser.newPage()
  
  user = "testingoli26@gmail.com" 
  password = 'Pepepecas1'
  
  await page.goto("https://trello.com/login")

  await page.waitForSelector("#user")
  await page.waitForSelector("#password")

  await page.type("#user", user)
  await page.type("#password", password)
  
  await page.click("#login")
  await page.goto("https://trello.com/b/QvHVksDa/personal-work-goals")
  
  print("Obteniendo tareas de Trello...")
  # Revisa los selectores que contiene la página
  selectores = await page.evaluate('() => { return Array.from(document.querySelectorAll("*"), element => element.tagName + (element.id ? "#" + element.id : "") + (element.className ? "." + element.className : "")) }')
  print(selectores)
  
  await page.waitForSelector("DIV#trello-root")
  tasks = await page.evaluate('''() => {
    const elements = Array.from(document.querySelectorAll("DIV#trello-root"));
    return elements.map(element => element.textContent);
}''')
  
  print(tasks);
  
  await browser.close()

  return tasks