from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your mixins here.


class AdminOnlyMixin(LoginRequiredMixin,UserPassesTestMixin):
    """Admin Only.
    TODO: Verify that an admin user has accessed
    """
    def test_func(self):
        return self.request.user.is_admin