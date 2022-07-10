import MainLayout from "layouts/MainLayout";
import UserProfile from "layouts/UserProfile";
import AdminPanel from "layouts/AdminPanel";

const routes = [
  {
    path: '/',
    component: MainLayout
  },
  {
    path: '/profile/:id',
    component: UserProfile,
  },
  {
    path:'/admin',
    component: AdminPanel,
  }
]

export default routes
