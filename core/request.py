from requests import (
    Response,
    request,
    HTTPError,
)
import allure

from core.exceptions import CustomBrokenException


def make_request(method: str, url: str, **kwargs) -> Response:
    with allure.step(f'Requests to {url}'):
        try:
            response = request(method=method, url=url, **kwargs)
        except HTTPError as e:
            raise CustomBrokenException(f'Error {e.response.status_code }during request to {url}') from e
    return response
