$(document).on('click','#see-more',function(){
    let nextPage = $(this).data('next-page');
      $.ajax({
        url: "{% url 'home' %}",  // Django URL for fetching paginated data
        type: 'GET',
        data: { page: nextPage },
        success: function(response) {
          const itemList = $('#topic-group-items');

          // Append new items to the list
          response.items.forEach(function(item) {
            itemList.append(`<li class="list-group-item">${item.name}</li>`);  // Replace 'name' with your field
          });

          // Show or hide the "See More" button based on whether there is a next page
          if (response.has_next) {
            $('#see-more').show();
            $('#see-more').data('next-page',response.next_page)  // Update to the next page number
            
          } else {
            $('#see-more').hide();
          }
        }
      });
  });
