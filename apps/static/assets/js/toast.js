// Toast message
// window.addEventListener('DOMContentLoaded', () => {
//     console.log('DOM fully loaded and parsed');
//     (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
//         const $notification = $delete.parentNode;

//         $delete.addEventListener('click', () => {
//             $notification.parentNode.removeChild($notification);
//         });
//     });
// });
var alert_del = document.querySelectorAll('.alert-del');
var to_delete = document.querySelectorAll('.to_delete');
const length = alert_del.length;
for (let i = 0; i < length; i++) {
    alert_del[i].addEventListener('click', function () {
        to_delete[i].parentNode.removeChild(to_delete[i])
    })
};