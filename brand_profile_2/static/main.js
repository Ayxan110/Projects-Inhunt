$(document).ready(function(){
    for(let i = 0; i < allImages.length; i++) {
        $('body').append('<h3 style="text-align:center;">' + items[i] + '</h3>')
        $('body').append('<div class="category flex row" style = "margin-bottom: 50px;  display: flex;justify-content: center;"></div>')
        const $currCategory = $('body .category:eq(-1)');
        $currCategory.append('<button type="button" class="btn prev btn-primary">Prev</button>')
        for(let j = 0; j < allImages[i].length; j++) {
            $currCategory.append('<img src="' + allImages[i][j] + '" alt="item" style="margin:5px;width: 15vw; min-width: 150px;margin-left: auto;margin-right: auto;  border: 5px solid #555;">')
        }
        // $currCategory.find('.count').html(`1 / ${$currCategory.find('img').length}`)
        $currCategory.append('<button type="button" class="btn next btn-primary">Next</button>')
        $currCategory.find('img:eq(0)').addClass('active')
        $currCategory.find('.next').click(function(){
            const $currImage = $currCategory.find('img.active')
            const $allCategoryImages = $currCategory.find('img')
            const currIndex = $allCategoryImages.index($currImage)
            $currCategory.find('img.active').removeClass('active')
            if (currIndex === $allCategoryImages.length - 1) {
                $allCategoryImages.eq(0).addClass('active')
            } else {
                $allCategoryImages.eq(currIndex + 1).addClass('active')
            }
            // $currCategory.find('count').html(`${$allCategoryImages.index($currCategory.find('img.active'))} / ${$allCategoryImages.length}`)
        })
        $currCategory.find('.prev').click(function(){
            const $currImage = $currCategory.find('img.active')
            const $allCategoryImages = $currCategory.find('img')
            const currIndex = $allCategoryImages.index($currImage)
            $currCategory.find('img.active').removeClass('active')
            if (currIndex === 0) {
                $allCategoryImages.eq(4).addClass('active')
            } else {
                $allCategoryImages.eq(currIndex - 1).addClass('active')
            }
            // $currCategory.find('count').html(`${$allCategoryImages.index($currCategory.find('img.active'))} / ${$allCategoryImages.length}`)
        })
    }
})