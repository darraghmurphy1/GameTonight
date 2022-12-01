from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib import messages


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 10


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for your comment!'
            )
        else:
            comment_form = CommentForm()
            messages.add_message(
                request,
                messages.ERROR,
                'Sorry! Please try again.'
            )

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class UserPostView(View):

    def get(self, request):
        """ Get  form  """

        post_form = PostForm()

        return render(
            request,
            'user_post.html',
            {
                'post_form': post_form,
            }
        )

    def post(self, request):

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(post_form.instance.title)
            post_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for your post'
            )
        else:
            post_form = PostForm()
            messages.add_message(
                request,
                messages.ERROR,
                'Please try again'
            )

        return HttpResponseRedirect(reverse('home'))


class PostEditView(View):
    """ View to allow user to edit their post """

    def get(self, request, id):
        """ Get question data and return a prefilled form """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        data = {'title': post.title, 'content': post.content}
        edit_form = PostForm(initial=data)

        return render(
            request,
            'edit_post.html',
            {
                'post': post,
                'edit_form': edit_form
            }
        )

    def post(self, request, id):
        """ This uses form data to update post
        """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        edit_form = PostForm(instance=post, data=request.POST)

        if edit_form.is_valid():
            post.title = edit_form.cleaned_data.get('title')
            post.content = edit_form.cleaned_data.get('content')
            post.slug = slugify(edit_form.cleaned_data.get('title'))
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'You edited your post successfully.'
            )

        else:
            edit_form = QuestionForm()
            messages.add_message(
                request,
                messages.WARNING,
                'The post has been updated.'
            )

        return HttpResponseRedirect(reverse('home'))


class PostDeleteView(View):
    """ This view allows to delete a post """

    def get(self, request, id):
        """ get post to delete """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        return render(
            request,
            'delete_post.html',
            {
                'post': post,
            }
        )

    def post(self, request, id):
        """ Delete the post """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        post.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            '{Post has been deleted.'
        )

        return HttpResponseRedirect(reverse('home'))
