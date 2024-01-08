// Function to create a new cart
function createCart() {
    return fetch('/store/carts/', {
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
        localStorage.setItem('cartId', data.id); // Store in local storage to persist across sessions
        return data.id;
    })
    .catch(error => {
        console.error('Error creating cart:', error);
        throw error;
    });
}

// Function to update the cart UI
function updateCartUI() {
    let cartId = localStorage.getItem('cartId');
    if (cartId) {
        fetch(`/store/carts/${cartId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error fetching cart data');
            }
            return response.json();
        })
        .then(cartData => {
            const cartCountElement = document.getElementById('cart-count');
            cartCountElement.textContent = cartData.items.length; // Update cart count

            const cartItemsListElement = document.getElementById('cart-items-list');
            cartItemsListElement.innerHTML = ''; // Clear current items
            cartData.items.forEach(item => {
                const li = document.createElement('li');
                li.className = 'cart-item';

                const imageSrc = item.product.images.length > 0 ? item.product.images[0].image : 'path/to/default/image.jpg';
                li.innerHTML = `
                    <img src="${imageSrc}" alt="${item.product.title}" class="cart-item-image">
                    <div class="cart-item-details">
                        <span class="cart-item-title">${item.product.title}</span>
                        <span class="cart-item-quantity">Qty: ${item.quantity}</span>
                        <span class="cart-item-price">$${(item.quantity * item.product.unit_price).toFixed(2)}</span>
                    </div>
                `;
                cartItemsListElement.appendChild(li);
            });

            // Add total price to the cart dropdown
            const totalLi = document.createElement('li');
            totalLi.className = 'cart-total';
            totalLi.textContent = `Total: $${cartData.total_price.toFixed(2)}`;
            cartItemsListElement.appendChild(totalLi);
        })
        .catch(error => {
            console.error('Error fetching cart:', error);
        });
    }
}

// Function to add an item to the cart
function addToCart(productId, quantity) {
    let cartId = localStorage.getItem('cartId');
    if (!cartId) {
        createCart().then(newCartId => {
            addToCart(productId, quantity); // Recursively call addToCart with the new cartId
        });
    } else {
        fetch(`/store/carts/${cartId}/items/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        })
        .then(response => response.json())
        .then(data => {
            updateCartUI(); // Update UI after adding to cart
        })
        .catch(error => console.error('Error:', error));
    }
}

// Helper function to get the CSRF token from cookies
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

// You would also need to implement the updateCartUI function to reflect changes in the UI.


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
    console.log('Toggled cart dropdown visibility.');
}

document.addEventListener('DOMContentLoaded', function() {
    let cartId = sessionStorage.getItem('cartId');
    if (cartId) {
        // Optionally, fetch cart details from server and update UI
        // fetch(`/store/carts/${cartId}`).then(...)...
    }
});


function toggleCart() {
    var cartDropdown = document.getElementById('cart-dropdown');
    if (cartDropdown.style.display === 'block') {
        cartDropdown.style.display = 'none';
    } else {
        cartDropdown.style.display = 'block';
        updateCartUI(); // This will update the cart UI when the dropdown is shown
    }
}
document.addEventListener('DOMContentLoaded', function() {
    updateCartUI(); // This function should be defined in 'CartFunctions.js'
});