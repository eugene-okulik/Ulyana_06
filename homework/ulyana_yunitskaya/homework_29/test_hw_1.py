from playwright.sync_api import Page, expect, Dialog


def test_with_alert(page: Page):

    def alert_mess(alert: Dialog):
        print(alert.message)
        alert.accept()

    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', alert_mess)
    page.get_by_role('link', name='Click').click()
    result = page.locator('#result')
    expect(result).to_contain_text('Ok')
