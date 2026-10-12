"""Tests for my own HW1 tool: check_refund_eligibility."""

from agent import tools
from agent.auth import AuthContext

SHOPPER_1 = AuthContext(user_id=1, role="shopper")
MERCHANT_STORE_2 = AuthContext(user_id=9002, role="merchant", store_id=2)


def test_outside_window_explains_why() -> None:
    result = tools.check_refund_eligibility(SHOPPER_1, 3980)
    assert result["ok"] is True
    assert result["eligible"] is False
    assert result["deadline"] == "2026-06-16"
    assert "closed" in result["reason"]


def test_eligible_order_gives_deadline() -> None:
    result = tools.check_refund_eligibility(SHOPPER_1, 4127)
    assert result["eligible"] is True
    assert result["deadline"] == "2026-07-19"
    assert result["needs_human_approval"] is False


def test_large_refund_needs_human() -> None:
    assert tools.check_refund_eligibility(SHOPPER_1, 4455)["needs_human_approval"] is True


def test_other_store_is_denied() -> None:
    result = tools.check_refund_eligibility(MERCHANT_STORE_2, 4127)
    assert result["error"] == "permission_denied"


def test_unknown_order() -> None:
    assert tools.check_refund_eligibility(SHOPPER_1, 999_999)["error"] == "not_found"
