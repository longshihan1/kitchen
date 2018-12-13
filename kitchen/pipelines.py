# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KitchenPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        """
        被 spider 调用，将 settings.py 传递进来，读取我们配置的参数
        模仿 images.py 源代码中的 from_settings 函数的写法
        """
        # 字典中的参数，要与 MySQLdb 中的connect 的参数相同
        dbparams = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset="utf8",
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )

        # twisted 中的 adbapi 能够将sql操作转变成异步操作
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用 twisted 将 mysql 操作编程异步执行
        """
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # handle exceptions

    def handle_error(self, failure):
        """
        处理异步操作的异常
        """
        print(failure)

    def do_insert(self, cursor, item):
        """
        执行具体的操作，能够自动 commit
        """
        image_download = json.dumps(item["front_img_url_download"])
        print(image_download)
        insert_sql = """
                    insert into bole_article(title, create_date, url, url_object_id, front_img_url, front_img_path, comment_nums, 
                    fav_nums, vote_nums, tags, content) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s', '%s','%s', '%s', '%s');
                """ % (item["title"], item["create_date"], item["url"], item["object_id"], image_download,
                       item["front_img_path"], item["comment_nums"], item["fav_nums"], item["vote_nums"], item["tags"],
                       item["content"])

        #cursor.execute(insert_sql, (item["title"], item["create_date"], item["url"], item["object_id"], image_download,
        #               item["front_img_path"], item["comment_nums"], item["fav_nums"], item["vote_nums"], item["tags"],
         #              item["content"]))
        print(insert_sql)
        cursor.execute(insert_sql)
