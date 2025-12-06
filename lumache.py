"""
lumache.py — Example module for Sphinx autodoc demonstration.

이 파일은 Sphinx autodoc 기능이 제대로 동작하는지 확인하기 위한 예제 모듈입니다.
PDF에서 설명한 구조를 그대로 따라 만든 예시입니다.
"""

def get_message(name: str) -> str:
    """
    사용자의 이름을 받아 인사 메시지를 반환합니다.

    Parameters
    ----------
    name : str
        인사 메시지에 사용될 사용자 이름

    Returns
    -------
    str
        인사 메시지 (예: "Hello, 석!")
    """
    return f"Hello, {name}!"


class Calculator:
    """
    간단한 사칙연산 계산기 클래스.

    이 클래스는 Sphinx autodoc의 클래스/메서드 문서화 예제를 보여주기 위한 것입니다.
    """

    def add(self, a: float, b: float) -> float:
        """
        두 숫자를 더한 값을 반환합니다.

        Parameters
        ----------
        a : float
            첫 번째 숫자
        b : float
            두 번째 숫자

        Returns
        -------
        float
            더한 값
        """
        return a + b

    def multiply(self, a: float, b: float) -> float:
        """
        두 숫자를 곱한 값을 반환합니다.

        Parameters
        ----------
        a : float
            첫 번째 숫자
        b : float
            두 번째 숫자

        Returns
        -------
        float
            곱한 값
        """
        return a * b
