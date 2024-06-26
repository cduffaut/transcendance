from django.urls import path
from .views import (
    account_information,
    user_dashboard,
    user_login,
    user_register,
    social_management,
    user_login_api,
    api_signup,
    logout_view,
    user_profile_pic_api,
    upload_profile_pic_api,
    test_upload,
    InviteListView,
    api_pending_invite,
    FriendListView,
    BlockedListView,
    search_usernames_api,
    profile_info_api,
    is_active_api,
    change_password_api,
    test_password_change_view,
    undo_invite_api,
    user_exist_api,
    is_blocked_api,
    profile_user,
    ColorView,
    forgot_password,
    email_sent,
    EmailValidation,
    PasswordForgot,
    change_password,
    PasswordReset,
    email_validated,
    error404,
    gameHistory_api,
    sendPasswordReset,
    update_profile_api,
)
from django.views.generic.base import RedirectView

urlpatterns = [
    path("error404/", error404, name="error404"),
    path("email_validated/", email_validated, name="email_validated"),
    path("change_password/", change_password, name="change_password"),
    path("email_sent/", email_sent, name="email_sent"),
    path("forgot_password/", sendPasswordReset.as_view(), name="forgot_password"),
    path("profile_user/", profile_user, name="profile_user"),
    path("accountInformation/", account_information, name="account_information"),
    path("dashboard/", user_dashboard, name="user_dashboard"),
    path("dashboard/<str:username>/", user_dashboard, name="user_dashboard_other"),
    path("login/", user_login, name="user_login"),
    path("register/", user_register, name="user_register"),
    path("socialManagement/", social_management, name="social_management"),
    path("", RedirectView.as_view(url="dashboard/", permanent=True)),
    path("api/login/", user_login_api, name="login_api"),
    path(
        "api/profile_pic/<str:username>/",
        user_profile_pic_api,
        name="user_profile_pic_api_other",
    ),
    path(
        "api/profile_pic/",
        user_profile_pic_api,
        name="user_profile_pic_api",
    ),
    path("api/upload_profile/", upload_profile_pic_api, name="upload_profile_pic_api"),
    path("api/signup/", api_signup, name="api_signup"),
    path("logout/", logout_view, name="user_logout"),
    path("test_upload/", test_upload),
    path(
        "api/invite/<str:username>/",
        InviteListView.as_view(),
        name="invite_user_api_other",
    ),
    path("api/invite/", InviteListView.as_view(), name="invite_user_api"),
    path("api/pending_invite/", api_pending_invite, name="pending_invite_api"),
    path("api/friends/", FriendListView.as_view(), name="friends_user_api"),
    path(
        "api/friends/<str:username>/",
        FriendListView.as_view(),
        name="friends_user_api_other",
    ),
    path("api/blocked/", BlockedListView.as_view(), name="blocked_user_api"),
    path(
        "api/blocked/<str:username>/",
        BlockedListView.as_view(),
        name="blocked_user_api_other",
    ),
    path(
        "api/search/<str:username>/", search_usernames_api, name="search_usernames_api"
    ),
    path(
        "api/profile/<str:username>/", profile_info_api, name="profile_info_api_other"
    ),
    path("api/profile/", profile_info_api, name="profile_info_api"),
    path("api/last_active/<str:username>/", is_active_api, name="is_active_api"),
    path("api/change_password/", change_password_api, name="change_password_api"),
    path("api/undo_invite/<str:username>/", undo_invite_api, name="undo_invite_api"),
    path("api/exist/<str:username>/", user_exist_api, name="user_exist_api"),
    path("api/is_blocked/<str:username>/", is_blocked_api, name="is_blocked_api"),
    path("api/colors/", ColorView.as_view(), name="color_api"),
    path(
        "api/mail/<str:username>/<str:token>/", EmailValidation, name="EmailValidation"
    ),
    path(
        "api/reset_password/<str:username>/<str:token>/",
        PasswordForgot,
        name="password forgot page",
    ),
    path("api/reset_password/change/", PasswordReset, name="password reset"),
    path("api/gameHistory/<str:username>/", gameHistory_api, name="gameHistory_api"),
    path("api/update_profile/", update_profile_api, name="update_profile_api"),
]
