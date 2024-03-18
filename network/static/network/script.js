document.addEventListener("DOMContentLoaded", () => {

    function getToken(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0,name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
        }
        return cookieValue;
    }
    var csrftoken = getToken('csrftoken')

    // Like / Unlike Posts
    // Profile view - Follow user
    if (document.getElementsByClassName('like-btn').length) {
        let btnsLike = document.getElementsByClassName('like-btn')

        for (let btnLike  of btnsLike) {
            btnLike.addEventListener('click', handleLike)
        }

        
        function handleLike(e) {
            e.preventDefault()

            let likeCounter, dataSet, heartBtn = null
            likeCounter = e.target.parentElement.querySelector('span')

            if (e.target.parentElement.parentElement.querySelector('span')) {
                likeCounter = e.target.parentElement.parentElement.querySelector('span')
                dataSet = e.target.parentElement.dataset
                heartBtn = e.target.parentElement.parentElement.querySelector('i')
            }
            if (e.target.parentElement.querySelector('a.like-btn')) {
                dataSet = e.target.parentElement.querySelector('a.like-btn').dataset
                heartBtn = e.target.parentElement.querySelector('a.like-btn i')
            }
            
            let likeCount = parseInt(likeCounter.innerHTML)
            let postId = dataSet.id
            let actionLike = dataSet.action
            
            // Save data in a variable
            data = {
                is_liked: actionLike,
                post_id: postId
            }
            
            // var url = `http://127.0.0.1:8000/like/`
            var url = window.location.origin + "/like/"
            fetch(url, {
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrftoken,
                }, 
                body:JSON.stringify(data) //JavaScript object of data to POST
            })
            .then((response) => {
                // console.log(response)
                return response.json(); //converts response to json
            })
            .then((data) => {
                // console.log('data:',data)
                if(data.result == 'success') {
                    //Perform actions with the response data from the view
                    if (actionLike == 'True') {
                        // Update like button appeareance to dislike
                        heartBtn.classList.remove('fa-solid')
                        heartBtn.classList.add('fa-regular')

                        // Update data action
                        dataSet.action = 'False'

                        // Sum 1 to like counter
                        likeCounter.innerHTML = String(likeCount - 1)
                    } 
                    else if (actionLike == 'False') {
                        // Update like button appeareance to dislike
                        heartBtn.classList.remove('fa-regular')
                        heartBtn.classList.add('fa-solid')

                        // Update data action
                        dataSet.action = 'True'

                        // Sum 1 to like counter
                        likeCounter.innerHTML = String(likeCount + 1)
                    }
                }
            });
        }
    }

    // Profile view - Follow user
    if (document.getElementById('follow-unfollow')) {

        const btnFollow = document.getElementById('follow-unfollow')
        const followCount = document.getElementById('follower-counter')
        
        let counter = parseInt(followCount.innerHTML)
        let userId = btnFollow.dataset.id
        let action = btnFollow.dataset.action
        
        btnFollow.addEventListener('click', handleFollow)
        
        function handleFollow() {
            
            let data = {
                action: action,
                user_id: userId
            }
            
            // var url = `http://127.0.0.1:8000/follow/`
            var url = window.location.origin + "/follow/"
            fetch(url, {
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrftoken,
                }, 
                body:JSON.stringify(data) //JavaScript object of data to POST
            })
            .then((response) => {
                // console.log(response)
                return response.json(); //converts response to json
            })
            .then((data) => {
                // console.log('data:',data)
                if(data.result == 'success') {
                    //Perform actions with the response data from the view
                    if (action == 'follow') {
                        // Update button to follow/unfollow
                        btnFollow.innerHTML = 'Unfollow'
                        btnFollow.setAttribute('data-action','unfollow')
                        btnFollow.classList.remove('btn-success')
                        btnFollow.classList.add('btn-danger')
                        action = btnFollow.dataset.action
                        // Update counter var
                        followCount.innerHTML = counter+1
                        counter = parseInt(followCount.innerHTML)
                    } 
                    else if (action == 'unfollow') {
                        // Update button to follow/unfollow
                        btnFollow.innerHTML = 'Follow'
                        btnFollow.setAttribute('data-action','follow')
                        btnFollow.classList.remove('btn-danger')
                        btnFollow.classList.add('btn-success')
                        action = btnFollow.dataset.action
                        // Update counter var
                        followCount.innerHTML = counter-1
                        counter = parseInt(followCount.innerHTML)
                    }
                }
            });
        }
    }

    // Editing posts - My posts
    if (document.getElementsByClassName('edit-post')) {
        let btnsEdit = document.getElementsByClassName('edit-post')

        for (let btnEdit  of btnsEdit) {
            btnEdit.addEventListener('click', handleEdit)
        }

        // Edit post
        function handleEdit(e) {
            e.preventDefault()
            // get post id
            let postId = e.target.dataset.id

            // select html elements
            let postCont = e.target.parentElement.parentElement
            let btnEdit = postCont.querySelector('button.edit-post')
            let textContainer = e.target.parentElement.parentElement.querySelector('p.content')
            let textContent = textContainer.innerHTML
            
            // hide old text content and edit button
            textContainer.style.display='none'
            btnEdit.style.display='none'

            // Create the form element
            const form = document.createElement('form');
            form.id='edit-form'

            // Create the input for content
            const contentTextArea = document.createElement('textarea');
            contentTextArea.name = 'content'; 
            contentTextArea.id = 'content';
            contentTextArea.rows = '3';
            contentTextArea.maxLength = '280';
            contentTextArea.classList.add('form-control');
            contentTextArea.value = textContent;

            // Create the submit input  
            const submitInput = document.createElement('input');
            submitInput.type = 'submit';
            submitInput.value = 'Save';
            submitInput.id = 'edit-post';
            submitInput.classList.add('btn')
            submitInput.classList.add('btn-primary')

            // Append the inputs to the form
            form.appendChild(contentTextArea);
            form.appendChild(submitInput);

            // Append the form to the post container
            postCont.appendChild(form);        

            // When submitting the form
            form.addEventListener("submit", (e) => {
                e.preventDefault();
                
                // fetch call to post_edit
                let data = {
                    post_id: postId,
                    content: contentTextArea.value
                }
                
                // var url = `http://127.0.0.1:8000/post_edit/`
                var url = window.location.origin + "/post_edit/"
                fetch(url, {
                    method:'POST',
                    headers:{
                        'Content-Type':'application/json',
                        'X-CSRFToken':csrftoken,
                    }, 
                    body:JSON.stringify(data) //JavaScript object of data to POST
                })
                .then((response) => {
                    // console.log(response)
                    return response.json(); //converts response to json
                })
                .then((data) => {
                    // console.log('data:',data)
                    if (data.result == 'success') {
                        // show new text content
                        textContainer.innerHTML=contentTextArea.value
                        textContainer.style.display='block'
                        btnEdit.style.display='block'
                        form.style.display='none'
                    }
                });
            });
        }
    }



});