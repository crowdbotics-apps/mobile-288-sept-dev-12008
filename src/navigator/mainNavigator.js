import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen211291Navigator from '../features/BlankScreen211291/navigator';
import BlankScreen111290Navigator from '../features/BlankScreen111290/navigator';
import BlankScreen011289Navigator from '../features/BlankScreen011289/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen211291: { screen: BlankScreen211291Navigator },
BlankScreen111290: { screen: BlankScreen111290Navigator },
BlankScreen011289: { screen: BlankScreen011289Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
