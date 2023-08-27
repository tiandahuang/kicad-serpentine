# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Serpentine Generation", pos = wx.DefaultPosition, size = wx.Size( 500,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.StatusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.StatusBar.SetToolTip( u"hello" )

		MainSizer = wx.BoxSizer( wx.VERTICAL )

		self.top_text = wx.StaticText( self, wx.ID_ANY, u"Size and Shape Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.top_text.Wrap( -1 )

		MainSizer.Add( self.top_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.paramguide = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"paramguide.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.paramguide, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		ParamsSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.r_label = wx.StaticText( self, wx.ID_ANY, u"Radius (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.r_label.Wrap( -1 )

		ParamsSizer.Add( self.r_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.r_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		ParamsSizer.Add( self.r_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.a_label = wx.StaticText( self, wx.ID_ANY, u"Amplitude (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.a_label.Wrap( -1 )

		ParamsSizer.Add( self.a_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.a_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		ParamsSizer.Add( self.a_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.alph_label = wx.StaticText( self, wx.ID_ANY, u"Alpha (deg)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alph_label.Wrap( -1 )

		ParamsSizer.Add( self.alph_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.alph_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		ParamsSizer.Add( self.alph_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.len_label = wx.StaticText( self, wx.ID_ANY, u"Length (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.len_label.Wrap( -1 )

		ParamsSizer.Add( self.len_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.len_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		ParamsSizer.Add( self.len_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pitch_label = wx.StaticText( self, wx.ID_ANY, u"Wire Spacing (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pitch_label.Wrap( -1 )

		ParamsSizer.Add( self.pitch_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pitch_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		ParamsSizer.Add( self.pitch_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edgedisable_label = wx.StaticText( self, wx.ID_ANY, u"Disable Edges", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.edgedisable_label.Wrap( -1 )

		ParamsSizer.Add( self.edgedisable_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edgedisable_value = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.CHK_2STATE )
		ParamsSizer.Add( self.edgedisable_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		MainSizer.Add( ParamsSizer, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MainSizer.Add( self.m_staticline1, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 20 )

		TraceParamsSizer = wx.GridSizer( 0, 3, 0, 0 )


		TraceParamsSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.wc_label = wx.StaticText( self, wx.ID_ANY, u"Wire Count", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wc_label.Wrap( -1 )

		TraceParamsSizer.Add( self.wc_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.width_label = wx.StaticText( self, wx.ID_ANY, u"Wire Width (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.width_label.Wrap( -1 )

		TraceParamsSizer.Add( self.width_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.f_cu_label = wx.StaticText( self, wx.ID_ANY, u"Front Copper", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.f_cu_label.Wrap( -1 )

		TraceParamsSizer.Add( self.f_cu_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.f_wc_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		TraceParamsSizer.Add( self.f_wc_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.f_width_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		TraceParamsSizer.Add( self.f_width_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.b_cu_label = wx.StaticText( self, wx.ID_ANY, u"Back Copper", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.b_cu_label.Wrap( -1 )

		TraceParamsSizer.Add( self.b_cu_label, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.b_wc_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		TraceParamsSizer.Add( self.b_wc_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.b_width_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		TraceParamsSizer.Add( self.b_width_value, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		MainSizer.Add( TraceParamsSizer, 1, wx.EXPAND, 5 )


		MainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		confirm_box = wx.StdDialogButtonSizer()
		self.confirm_boxOK = wx.Button( self, wx.ID_OK )
		confirm_box.AddButton( self.confirm_boxOK )
		self.confirm_boxApply = wx.Button( self, wx.ID_APPLY )
		confirm_box.AddButton( self.confirm_boxApply )
		self.confirm_boxCancel = wx.Button( self, wx.ID_CANCEL )
		confirm_box.AddButton( self.confirm_boxCancel )
		confirm_box.Realize();

		MainSizer.Add( confirm_box, 0, wx.EXPAND, 5 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.r_value.Bind( wx.EVT_TEXT_ENTER, self.RadiusParamEvent )
		self.a_value.Bind( wx.EVT_TEXT_ENTER, self.AmplitudeParamEvent )
		self.alph_value.Bind( wx.EVT_TEXT_ENTER, self.AlphaParamEvent )
		self.len_value.Bind( wx.EVT_TEXT_ENTER, self.LengthParamEvent )
		self.pitch_value.Bind( wx.EVT_TEXT_ENTER, self.WirePitchParamEvent )
		self.edgedisable_value.Bind( wx.EVT_CHECKBOX, self.EdgeDisableParamEvent )
		self.f_wc_value.Bind( wx.EVT_TEXT_ENTER, self.FWCParamEvent )
		self.f_width_value.Bind( wx.EVT_TEXT_ENTER, self.FWidthParamEvent )
		self.b_wc_value.Bind( wx.EVT_TEXT_ENTER, self.BWCParamEvent )
		self.b_width_value.Bind( wx.EVT_TEXT_ENTER, self.BWidthParamEvent )
		self.confirm_boxApply.Bind( wx.EVT_BUTTON, self.ApplyEvent )
		self.confirm_boxCancel.Bind( wx.EVT_BUTTON, self.CancelEvent )
		self.confirm_boxOK.Bind( wx.EVT_BUTTON, self.ValidateEvent )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def RadiusParamEvent( self, event ):
		event.Skip()

	def AmplitudeParamEvent( self, event ):
		event.Skip()

	def AlphaParamEvent( self, event ):
		event.Skip()

	def LengthParamEvent( self, event ):
		event.Skip()

	def WirePitchParamEvent( self, event ):
		event.Skip()

	def EdgeDisableParamEvent( self, event ):
		event.Skip()

	def FWCParamEvent( self, event ):
		event.Skip()

	def FWidthParamEvent( self, event ):
		event.Skip()

	def BWCParamEvent( self, event ):
		event.Skip()

	def BWidthParamEvent( self, event ):
		event.Skip()

	def ApplyEvent( self, event ):
		event.Skip()

	def CancelEvent( self, event ):
		event.Skip()

	def ValidateEvent( self, event ):
		event.Skip()


###########################################################################
## Class ErrorDialog
###########################################################################

class ErrorDialog ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		MainSizer = wx.BoxSizer( wx.VERTICAL )

		self.message = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.message.Wrap( -1 )

		MainSizer.Add( self.message, 0, wx.ALL|wx.EXPAND, 5 )


		MainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		confirm_box = wx.StdDialogButtonSizer()
		self.confirm_boxOK = wx.Button( self, wx.ID_OK )
		confirm_box.AddButton( self.confirm_boxOK )
		confirm_box.Realize();

		MainSizer.Add( confirm_box, 0, wx.EXPAND, 5 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.message.Bind( wx.EVT_SIZE, self.ResizeEvent )
		self.confirm_boxOK.Bind( wx.EVT_BUTTON, self.ValidateEvent )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ResizeEvent( self, event ):
		event.Skip()

	def ValidateEvent( self, event ):
		event.Skip()


