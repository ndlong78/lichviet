from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Đảm bảo database và tables được tạo
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8080)