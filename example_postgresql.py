import psycopg

with psycopg.connect("host=10.10.10.10 port=5432 dbname=postgres user=postgres password=password") as connection:

    with connection.cursor() as cursor:

        try:
            # 테이블 생성 쿼리 실행
            cursor.execute("""
                        CREATE TABLE example(
                            note text,
                            username text)
                        """)

            # Insert 쿼리 실행
            result = cursor.execute("""
                            INSERT INTO example(note, username) VALUES(%s, %s)
                            """,
                            ("test!", "hong"))

            connection.commit()

            print(f"changed rows: {result}")

            cursor.execute("SELECT * FROM example")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
