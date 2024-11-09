from controller.base_controller import BaseController
from model.article import ArticleModel
from view.article_view import ArticleView

class ArticleController(BaseController):
    def __init__(self, root):
        self.model = ArticleModel()
        self.view = ArticleView(root, self)

    def create_article(self):
        title = "New Article"
        content = "This is the content of the new article"
        if self.model.create_article(title, content):
            print("Article created successfully!")
        else:
            print("Error: Missing title or content")

    def update_article(self):
        pass

    def delete_article(self):
        pass
