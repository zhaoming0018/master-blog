# -*- coding:utf-8 -*-
from db.DB import db
def create_database_blog():
    db.connect("blog")
    create_user = """
    CREATE TABLE IF NOT EXISTS USER (
        USERID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME VARCHAR(50) NOT NULL,
        PASSWORD VARCHAR(50) NOT NULL,
        EMAIL VARCHAR(50),
        CREATE_TIME DATETIME NOT NULL,
        VALID BOOLEAN DEFAULT TRUE
    )
    """
    db.execute_sql(create_user)

    create_article = """
    CREATE TABLE IF NOT EXISTS ARTICLE (
        ARTICLEID INTEGER PRIMARY KEY AUTOINCREMENT,
        CREATE_TIME DATETIME NOT NULL,
        TITLE VARCHAR(255) NOT NULL,
        TAGS VARCHAR(255),
        LIKES_NUM INTEGER DEFAULT 0,
        DISLIKES_NUM INTEGER DEFAULT 0,
        VALID BOOLEAN DEFAULT TRUE,
        AUTHORID INTEGER NOT NULL,
        CONTENT TEXT NOT NULL,
        MARK VARCHAR(32)
    )
    """
    db.execute_sql(create_article)

    create_comment = """
    CREATE TABLE IF NOT EXISTS COMMENT (
        COMMENTID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICLEID INTEGER NOT NULL,
        FLOORID INTEGER NOT NULL,
        CREATE_TIME DATETIME NOT NULL,
        LIKES_NUM INTEGER DEFAULT 0,
        DISLIKES_NUM INTEGER DEFAULT 0,
        USERID INTEGER NOT NULL
    )
    """
    db.execute_sql(create_comment)

    create_like_for_article = """
    CREATE TABLE IF NOT EXISTS LIKE_FOR_ARTICLE (
        LIKEID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICLEID INTEGER NOT NULL,
        USERID INTEGER NOT NULL,
        CREATE_TIME DATETIME NOT NULL,
        VALID BOOLEAN DEFAULT TRUE
    )
    """
    db.execute_sql(create_like_for_article)

    create_unlike_for_article = """
    CREATE TABLE IF NOT EXISTS UNLIKE_FOR_ARTICLE (
        UNLIKEID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICLEID INTEGER NOT NULL,
        USERID INTEGER NOT NULL,
        CREATE_TIME DATETIME NOT NULL,
        VALID BOOLEAN DEFAULT TRUE
    )
    """
    db.execute_sql(create_unlike_for_article)

    create_like_for_comment = """
    CREATE TABLE IF NOT EXISTS LIKE_FOR_COMMENT (
        LIKEID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICLEID INTEGER NOT NULL,
        USERID INTEGER NOT NULL,
        CREATE_TIME DATETIME NOT NULL,
        VALID BOOLEAN DEFAULT TRUE
    )
    """
    db.execute_sql(create_like_for_comment)

    create_unlike_for_comment = """
    CREATE TABLE IF NOT EXISTS UNLIKE_FOR_COMMENT (
        UNLIKEID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICLEID INTEGER NOT NULL,
        USERID INTEGER NOT NULL,
        CREATE_TIME DATETIME NOT NULL,
        VALID BOOLEAN DEFAULT TRUE
    )
    """
    db.execute_sql(create_unlike_for_comment)

    create_login_info = """
    CREATE TABLE IF NOT EXISTS LOGIN_INFO (
        INFOID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERID INTEGER NOT NULL,
        IP CHAR(16) NOT NULL,
        LOGTIME DATETIME NOT NULL
    )
    """
    db.execute_sql(create_login_info)