import MainLayout from "layouts/MainLayout";
import UserProfile from "layouts/UserProfile";

const routes = [
  {
    path: '/',
    component: MainLayout
  },
  {
    path: '/profile/:id',
    component: UserProfile,
    props: (route) => route.id
  },
]

export default routes
