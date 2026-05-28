from playwright.sync_api import Page


def test_student_registration_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Ulyana')
    page.get_by_placeholder('Last Name').fill('Yunitskaya')
    page.locator('#userEmail').fill('qaws@mail.ru')
    page.locator('#userNumber').fill('4852525252')
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__month-select').select_option('10')
    page.locator('.react-datepicker__year-select').select_option('1994')
    page.locator('.react-datepicker__day--006').first.click()
    page.locator('#subjectsInput').fill('Math')
    page.get_by_placeholder('Current Address').fill('ul.Krol, h.10')
    page.locator('#state').click(force=True)
    page.get_by_text('NCR', exact=True).click()
    page.locator('#city').click(force=True)
    page.get_by_text('Noida', exact=True).click()
    page.locator('label[for="hobbies-checkbox-2"]').click()
    page.locator('label[for="gender-radio-2"]').click()
    page.get_by_role('button', name='Submit').click()
