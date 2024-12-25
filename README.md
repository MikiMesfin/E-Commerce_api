# E-commerce API

A comprehensive RESTful API for an e-commerce platform built with Django REST Framework, featuring complete product management, user authentication, and advanced features like wishlists and promotions.

## Features

### Core Features
- **Product Management**
  - CRUD operations for products
  - Category management
  - Stock tracking
  - Multiple product images
  - Price management with discounts
  
- **User Management**
  - User registration and authentication
  - JWT-based authentication
  - Role-based access control
  - User profiles

- **Shopping Features**
  - Wishlist functionality
  - Product reviews and ratings
  - Advanced product search
  - Category-based browsing
  - Stock management

### Technical Features
- RESTful API design
- JWT authentication
- Comprehensive API documentation
- Advanced filtering and search
- Pagination
- Rate limiting
- Custom exception handling
- Automated stock notifications

## Technology Stack

- Python 3.8+
- Django 5.1
- Django REST Framework
- PostgreSQL (optional, configurable)
- JWT Authentication
- Swagger/OpenAPI Documentation

## Installation

1. **Clone the Repository**   ```bash
   git clone <repository-url>
   cd ecommerce-api   ```

2. **Set Up Virtual Environment**   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate   ```

3. **Install Dependencies**   ```bash
   pip install -r requirements.txt   ```

4. **Environment Setup**
   Create a `.env` file in the root directory:   ```
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password   ```

5. **Database Setup**   ```bash
   python manage.py migrate   ```

6. **Create Superuser**   ```bash
   python manage.py createsuperuser   ```

7. **Run Development Server**   ```bash
   python manage.py runserver   ```

## API Endpoints

### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token
- `POST /api/users/register/` - Register new user
- `GET /api/users/profile/` - Get user profile

### Products
- `GET /api/products/` - List all products
- `POST /api/products/` - Create new product (Admin only)
- `GET /api/products/{id}/` - Get product details
- `PUT /api/products/{id}/` - Update product (Admin only)
- `DELETE /api/products/{id}/` - Delete product (Admin only)

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create new category (Admin only)

### Reviews
- `POST /api/products/{id}/reviews/` - Create product review
- `GET /api/products/{id}/reviews/` - List product reviews

### Wishlist
- `GET /api/wishlist/` - Get user's wishlist
- `POST /api/products/{id}/wishlist/` - Add product to wishlist
- `DELETE /api/products/{id}/wishlist/` - Remove from wishlist

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Testing

Run the test suite:
```bash
python manage.py test
```

For coverage report:
```bash
coverage run --source='.' manage.py test
coverage report
```

## Development

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings for all functions and classes

### Contributing
1. Create a new branch for each feature
2. Write tests for new features
3. Ensure all tests pass before submitting PR
4. Update documentation as needed

## Security Features

- JWT-based authentication
- Permission-based access control
- Rate limiting
- SSL/TLS support
- XSS protection
- CSRF protection

## Production Deployment

### Checklist
1. Set DEBUG=False
2. Configure proper ALLOWED_HOSTS
3. Use strong SECRET_KEY
4. Set up proper database (PostgreSQL recommended)
5. Configure HTTPS
6. Set up proper email backend
7. Configure static files serving
8. Set up proper logging

### Example Production Settings
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## Monitoring and Maintenance

- Regular database backups
- Monitor server logs
- Track API usage and performance
- Monitor stock levels
- Regular security updates

## Support

For support, please contact:
- Email: mikimesfin45@gmail.com
- Issue Tracker: GitHub Issues

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

This README provides:
- Comprehensive feature list
- Detailed installation instructions
- Complete API endpoint documentation
- Security considerations
- Development guidelines
- Production deployment checklist
- Monitoring recommendations

