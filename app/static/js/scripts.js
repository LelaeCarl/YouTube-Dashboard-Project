// static/js/scripts.js
function createChart(id, type, data) {
    const ctx = document.getElementById(id);
    new Chart(ctx, {
        type: type,
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: id === 'viewsChart' ? 'Views by Video' : 'Top Video Tags'
                }
            }
        }
    });
}
