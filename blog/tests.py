from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Tag, Post, Comment

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.category = Category.objects.create(name='Test Category')
        self.tag = Tag.objects.create(name='Test Tag')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='This is a test post.',
            author=self.user,
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='This is a test comment.',
        )

    def test_post_list_view(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        url = reverse('blog:post_detail', args=[self.post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('blog:post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_post_create_submit_form(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('blog:post_create')
        data = {
            'title': 'New Test Post',
            'content': 'This is a new test post.',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        self.assertEqual(Post.objects.count(), 2)  # Check if the post is created
        self.assertTrue(Post.objects.filter(title='New Test Post').exists())

    def test_post_detail_view_with_comment(self):
        url = reverse('blog:post_detail', args=[self.post.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')
        self.assertContains(response, 'This is a test comment.')

    def test_invalid_post_detail_view(self):
        url = reverse('blog:post_detail', args=['invalid-slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_comment_creation(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('blog:post_detail', args=[self.post.slug])
        data = {
            'content': 'Another test comment.',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after comment submission
        self.assertEqual(Comment.objects.count(), 2)  # Check if the comment is created
        self.assertTrue(Comment.objects.filter(content='Another test comment.').exists())

    def test_category_str_representation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_tag_str_representation(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_str_representation(self):
        self.assertEqual(str(self.comment), f"Comment by {self.user.username} on Test Post")
