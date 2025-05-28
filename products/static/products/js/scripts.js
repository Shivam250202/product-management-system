// Product-specific JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Product scripts loaded');
    
    // Example: Confirm before deleting
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this product?')) {
                e.preventDefault();
            }
        });
    });
});