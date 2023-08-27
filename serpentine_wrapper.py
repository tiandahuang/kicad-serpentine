import wx
import serpentine_gui as gui
# import serpentine_utils as utils
import functools as ft

class SerpentineGUI(gui.MainFrame):

    def __init__(self, parent, validate_func, run_func):
        super(SerpentineGUI, self).__init__(parent)

        self.validate_func = validate_func
        self.run_func = run_func

        def call2(f_inner, f_outer, *args, **kwargs):
            return f_outer(f_inner(*args, **kwargs))
        
        def wx_textctrl_getvalue(wx_obj, **validate_kwargs):
            return ft.partial(call2, 
                              wx_obj.GetValue, 
                              ft.partial(self.validate_num, **validate_kwargs))

        def wx_textctrl_setvalue(wx_obj):
            return ft.partial(call2, str, wx_obj.SetValue)


        self.param_getters = {
                'radius':   wx_textctrl_getvalue(self.r_value, lo=0),
                'amplitude':wx_textctrl_getvalue(self.a_value, lo=0),
                'alpha':    wx_textctrl_getvalue(self.alph_value, lo=0, hi=90),
                'length':   wx_textctrl_getvalue(self.len_value, lo=0),
                'pitch':    wx_textctrl_getvalue(self.pitch_value, lo=0),
                'f_wc':     wx_textctrl_getvalue(self.f_wc_value, lo=0, type_conv=int),
                'f_width':  wx_textctrl_getvalue(self.f_width_value, lo=0),
                'b_wc':     wx_textctrl_getvalue(self.b_wc_value, lo=0, type_conv=int),
                'b_width':  wx_textctrl_getvalue(self.b_width_value, lo=0),
                'noedge':   self.edgedisable_value.GetValue,
        }

        self.param_setters = {
                'radius':   wx_textctrl_setvalue(self.r_value),
                'amplitude':wx_textctrl_setvalue(self.a_value),
                'alpha':    wx_textctrl_setvalue(self.alph_value),
                'length':   wx_textctrl_setvalue(self.len_value),
                'pitch':    wx_textctrl_setvalue(self.pitch_value),
                'f_wc':     wx_textctrl_setvalue(self.f_wc_value),
                'f_width':  wx_textctrl_setvalue(self.f_width_value),
                'b_wc':     wx_textctrl_setvalue(self.b_wc_value),
                'b_width':  wx_textctrl_setvalue(self.b_width_value),
                'noedge':   self.edgedisable_value.SetValue,
        }

        self.param_defaults = {
                'radius':   1,
                'amplitude':1,
                'alpha':    0,
                'length':   10,
                'pitch':    0.2,
                'f_wc':     1,
                'f_width':  0.2,
                'b_wc':     1,
                'b_width':  0.2,
                'noedge':   False,
        }

        for param, val in self.param_defaults.items():
            self.param_setters[param](val)
        self.params = {param:self.param_getters[param]() for param in self.param_getters}

    # event handlers

    def RadiusParamEvent(self, event):
        event_str = 'radius'
        self.param_event_handler(event_str)

    def AmplitudeParamEvent(self, event):
        event_str = 'amplitude'
        self.param_event_handler(event_str)

    def AlphaParamEvent(self, event):
        event_str = 'alpha'
        self.param_event_handler(event_str)

    def LengthParamEvent(self, event):
        event_str = 'length'
        self.param_event_handler(event_str)

    def WirePitchParamEvent(self, event):
        event_str = 'pitch'
        self.param_event_handler(event_str)

    def EdgeDisableParamEvent(self, event):
        event_str = 'noedge'
        self.param_event_handler(event_str)

    def FWCParamEvent(self, event):
        event_str = 'f_wc'
        self.param_event_handler(event_str)

    def FWidthParamEvent(self, event):
        event_str = 'f_width'
        self.param_event_handler(event_str)

    def BWCParamEvent(self, event):
        event_str = 'b_wc'
        self.param_event_handler(event_str)

    def BWidthParamEvent(self, event):
        event_str = 'b_width'
        self.param_event_handler(event_str)

    def ApplyEvent(self, event):
        event_str = 'apply'
        self.log(event_str)
        status, errmsg = self.validate_func(self.params)
        if not status:
            self.error(errmsg)
        self.run_func(self.params)
        wx.Exit()

    def CancelEvent(self, event):
        event_str = 'cancel'
        self.log(event_str)
        wx.Exit()

    def ValidateEvent(self, event):
        event_str = 'validate'
        self.log(str(self.params))
        status, errmsg = self.validate_func(self.params)
        if not status:
            self.error(errmsg)

    # helper methods

    def log(self, t):
        self.StatusBar.SetStatusText(t)
    
    def error(self, t):
        frame = self.SerpentineError(self, t)
        frame.Show(True)

    def param_event_handler(self, event_str):
        val = self.param_getters[event_str]()
        if val is not None:
            self.params[event_str] = val
        else:
            self.param_setters[event_str](self.params[event_str])
        self.log(f'{event_str} set to {self.params[event_str]}')

    @staticmethod
    def validate_num(val, lo=None, hi=None, clip=False, type_conv=float):
        try:
            f = type_conv(val)
        except ValueError as e:
            return None

        if lo is not None or hi is not None:
            if lo is None: lo = -float('inf')
            if hi is None: hi = float('inf')
            if clip:
                f = type_conv(min(max(f, lo), hi))
            else:
                if f > hi or f < lo:
                    return None
        
        return f
    
    class SerpentineError(gui.ErrorDialog):

        def __init__(self, parent, text):
            super(SerpentineGUI.SerpentineError, self).__init__(parent)
            self.text = text
            self.text_width = 0

        def ResizeEvent(self, event):
            new_width = self.GetSize().width
            if abs(self.text_width - new_width) > 20:
                self.message.SetLabel(self.text)
                self.text_width = new_width
            self.message.Wrap(new_width - 20)

        def ValidateEvent(self, event):
            self.Destroy()


class SerpentineWrapper():

    def __init__(self):
        app = wx.App(False)
        frame = SerpentineGUI(None, self.validate, self.run)
        frame.Show(True)
        app.MainLoop()

    @staticmethod
    def validate(a):
        print(a)
        return True, None
    
    @staticmethod
    def run(a):
        print(a)
        return True, None

if __name__ == '__main__':

    SerpentineWrapper()
