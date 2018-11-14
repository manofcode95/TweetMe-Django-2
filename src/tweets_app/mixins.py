class AddUserToForm():
    def form_valid(self, form):
        if form.is_valid():
            form.instance.user=self.request.user
            return super(AddUserToForm, self).form_valid(form)
        form.add_error(None, 'Form is not valid. Please try again')
        return super(AddUserToForm, self).form_invalid(form)

class UserOwnerMixin():
    def form_valid(self, form):
        if self.request.user != form.instance.user:
            form.add_error(None, 'Only the owner of this post be able to update')
            return super(UserOwnerMixin, self).form_invalid(form)
        else:
            return super(UserOwnerMixin, self).form_valid(form)  