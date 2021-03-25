import pytest

from final.pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    @pytest.mark.personal_test
    def test_guest_can_log_in_with_correct_data(self, browser):
        # Arrange
        email = "pent2006@gmail.com"
        password = "bcMLkabAijX25hF"
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        page.login_with_correct_data(email, password)

        # Assert
        page.should_be_login_in()

    @pytest.mark.personal_test
    def test_guest_cant_log_in_with_incorrect_data(self, browser):
        # Arrange
        email = "pent1990@gmail.com"
        password = "bcMLkabAijX25hF"
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        page.login_with_correct_data(email, password)

        # Assert
        page.should_not_be_login_in()

    @pytest.mark.personal_test
    def test_quest_can_go_to_reset_password(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        page.go_to_reset_password_page()

        # Assert
        page.should_be_forgotten_password_form()
