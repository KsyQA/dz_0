from selene.support.shared import browser
from selene import be, have

browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id="firstName"]').should(be.blank).type('Misha')
browser.element('[id="lastName"]').type('Abishev')
browser.element('[id="userEmail"]').type('some@email.ru')
browser.element('[id="userNumber"]').type('9876543211')
browser.element('[for = "hobbies-checkbox-1"]').click()
browser.element('[for = "hobbies-checkbox-2"]').click()
browser.element('[for = "hobbies-checkbox-3"]').click()
browser.config.hold_browser_open = True