class SocialNetwork:
    """
    Базовый класс для социальных сетей
    """

    def __init__(self, name: str, user_count: int) -> None:
        """
        Инициализация экземпляра социальной сети

        :param name: название
        :param user_count: кол-во пользователей
        """
        self.name = name
        self.user_count = user_count

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта

        :return: строка с названием и количеством пользователей
        """
        return f"{self.name} имеет {self.user_count} пользователей."

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта

        :return: строковое представление объекта
        """
        return f"SocialNetwork(name='{self.name}', user_count={self.user_count})"

    def post(self, message: str) -> str:
        """
        публикация сообщение в социальной сети

        :param message: сообщение для публикации
        :return: подтверждение
        """
        return f"Сообщение '{message}' опубликовано на {self.name}."


class VK(SocialNetwork):
    """
    Класс для социальной сети VK.
    """

    def __init__(self, user_count: int, has_video: bool) -> None:
        """
        инициализирует экземпляр VK, наследуя от SocialNetwork

        :param user_count: количество пользователей
        :param has_video: наличие видеозаписей
        """
        super().__init__("VK", user_count)
        self.has_video = has_video

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта VK

        :return: Строка с названием и количеством пользователей, а также информацией о видео.
        """
        video_info = "имеет" if self.has_video else "не имеет"
        return f"{self.name} имеет {self.user_count} пользователей и {video_info} видеозаписи."

    def video_feature(self) -> str:
        """
        Предоставляет информацию о функции видеозаписей.

        :return: информация о наличии видеозаписей.
        """
        return "VK поддерживает видео." if self.has_video else "VK не поддерживает видео."


class Facebook(SocialNetwork):
    """
    Класс для социальной сети Facebook.
    """

    def __init__(self, user_count: int, is_marketplace_available: bool) -> None:
        """
        Инициализирует экземпляр Facebook, наследуя от SocialNetwork.

        :param user_count: кол-во пользователей.
        :param is_marketplace_available: доступность маркетплейса.
        """
        super().__init__("Facebook", user_count)
        self.is_marketplace_available = is_marketplace_available

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Facebook.

        :return: Официальное строковое представление объекта.
        """
        return (f"Facebook(user_count={self.user_count}, "
                f"is_marketplace_available={self.is_marketplace_available})")

    def marketplace_info(self) -> str:
        """
        Предоставляет информацию о функции маркетплейса.

        :return: Информация о доступности маркетплейса.
        """
        return "Facebook имеет Marketplace." if self.is_marketplace_available else "Facebook не имеет Marketplace."


if __name__ == "__main__":
    vk = VK(user_count=45000000, has_video=True)
    print(vk)
    print(vk.post("Привет, мир!"))
    print(vk.video_feature())

    facebook = Facebook(user_count=2900000000, is_marketplace_available=True)
    print(facebook)
    print(facebook.post("Hello, world!"))
    print(facebook.marketplace_info())

    pass
