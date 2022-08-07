class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state for Television.
        :param MIN_CHANNEL: Initial minimum channel set to default 0.
        :param MIN_VOLUME: Initial minimum volume set to default 3.
        """
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to change Television power status.
        :return: Power status.
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method to change the channel up.
        :return: Current channel plus 1.
        """
        if self.__status == True and self.__channel < self.MAX_CHANNEL:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to change the channel down.
        :return: Current channel minus 1.
        """
        if self.__status == True and self.__channel > self.MAX_CHANNEL:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to change the volume level up.
        :return: Current volume level plus 1.
        """
        if self.__status == True and self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to change the volume level down.
        :return: Current volume level minus 1.
        """
        if self.__status == True and self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Return statement which provides: power status, current channel, current volume.
        """
        return 'TV status: Is on = ' + str(self.__status) + ', Channel = ' + str(self.__channel) + ', Volume = ' + str(
            self.__volume)
