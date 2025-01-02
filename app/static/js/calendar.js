document.addEventListener('DOMContentLoaded', function() {
    // Event handlers
    setupEventHandlers();
    // Initialize calendar
    initializeCalendar();
});

function setupEventHandlers() {
    // Event click handler
    document.querySelectorAll('.event').forEach(event => {
        event.addEventListener('click', function(e) {
            const eventId = this.dataset.eventId;
            showEventDetails(eventId);
        });
    });

    // Add event button handler
    document.querySelector('.add-event-btn')?.addEventListener('click', function() {
        showEventForm();
    });
}

function showEventDetails(eventId) {
    fetch(`/api/events/${eventId}`)
        .then(response => response.json())
        .then(event => {
            // Show event details in modal
            const modal = document.getElementById('event-modal');
            modal.querySelector('.event-title').textContent = event.title;
            modal.querySelector('.event-time').textContent = 
                `${event.start_time} - ${event.end_time}`;
            modal.querySelector('.event-description').textContent = 
                event.description;
            modal.style.display = 'block';
        });
}

function showEventForm(date = null) {
    const form = document.getElementById('event-form');
    if (date) {
        form.querySelector('[name="date"]').value = date;
    }
    form.style.display = 'block';
}

function initializeCalendar() {
    // Add current date highlight
    const today = new Date();
    const currentDay = document.querySelector(
        `[data-date="${today.toISOString().split('T')[0]}"]`
    );
    if (currentDay) {
        currentDay.classList.add('today');
    }
}