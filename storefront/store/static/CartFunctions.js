function createCart() {
    return fetch('/store/carts/', {  // Adjust the URL to match your API endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        credentials: 'include' 
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Cart created:', data);
        sessionStorage.setItem('cartId', data.id);
        return data.id;
    })
    .catch(error => {
        console.error('Error creating cart:', error);
        throw error;
    });
}

function addToCart(productId, quantity) {
    let cartId = sessionStorage.getItem('cartId');

    if (!cartId) {
        createCart().then(() => {
            cartId = sessionStorage.getItem('cartId');
            addToCart(productId, quantity);
        });
    } else {
        fetch(`/store/carts/${cartId}/items/`, {  // Adjust the URL to match your API endpoint for adding items
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Added to cart:', data);
            updateCartUI(data);  // Assuming you have an updateCartUI function to update the UI
        })
        .catch(error => console.error('Error:', error));
    }
}

function updateCartItem(cartItemId, quantity) {
    const cartId = sessionStorage.getItem('cartId');
    fetch(`/store/carts/${cartId}/items/${cartItemId}/`, {  // Adjust the URL to match your API endpoint for updating items
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ quantity: quantity })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Updated cart item:', data);
        updateCartUI(data);
    })
    .catch(error => console.error('Error:', error));
}

function removeCartItem(cartItemId) {
    const cartId = sessionStorage.getItem('cartId');
    fetch(`/store/carts/${cartId}/items/${cartItemId}/`, {  // Adjust the URL to match your API endpoint for removing items
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (response.ok) {
            console.log('Removed cart item');
            updateCartUI();  // Call to update UI after item removal
        }
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toggleCart() {
    const cartDropdown = document.getElementById('cart-dropdown');
    cartDropdown.style.display = cartDropdown.style.display === 'block' ? 'none' : 'block';
}

function updateCartUI(cartItems) {
    // Implementation for updating cart UI
    // This function needs to be implemented according to your UI design
}

document.addEventListener('DOMContentLoaded', function() {
    let cartId = sessionStorage.getItem('cartId');
    if (cartId) {
        // Optionally, fetch cart details from server and update UI
        // fetch(`/store/carts/${cartId}`).then(...)...
    }
});
